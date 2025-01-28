document.addEventListener("DOMContentLoaded", function () {
    const qualificationField = document.querySelector("#id_current_qualification");
    const allFields = {
        twelfth: ["twelfth_school_name", "twelfth_marks", "twelfth_field"],
        diploma: ["diploma_institution_name", "diploma_field", "diploma_percentage"],
        ug: ["ug_college_name", "ug_degree", "ug_branch", "ug_percentage"],
        pg: ["pg_college_name", "pg_degree", "pg_branch", "pg_percentage"],
    };

    function hideFields(fieldsToHide) {
        for (const field in allFields) {
            const fields = allFields[field];
            fields.forEach(fieldId => {
                const element = document.getElementById(`id_${fieldId}`);
                if (element) {
                    element.parentElement.style.display = fieldsToHide.includes(fieldId) ? "none" : "block";
                }
            });
        }
    }

    function updateFieldVisibility() {
        const qualification = qualificationField.value;
        switch (qualification) {
            case "10":
                hideFields([...allFields.twelfth, ...allFields.diploma, ...allFields.ug, ...allFields.pg]);
                break;
            case "12":
                hideFields([...allFields.diploma, ...allFields.ug, ...allFields.pg]);
                break;
            case "Diploma":
                hideFields([...allFields.twelfth, ...allFields.ug, ...allFields.pg]);
                break;
            case "UG":
                hideFields([...allFields.pg]);
                break;
            default:
                hideFields([]);
        }
    }

    qualificationField.addEventListener("change", updateFieldVisibility);
    updateFieldVisibility();
});
