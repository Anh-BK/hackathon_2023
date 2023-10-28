import { CheckboxGroup } from "@nextui-org/react";
import { CustomCheckbox } from "./CheckBox";
import React from "react";
import { companies } from "../../constants/company";

export function CheckboxGroupCustom() {
  const [groupSelected, setGroupSelected] = React.useState([]);

  return (
    <div className="flex flex-col gap-1 w-full">
      <CheckboxGroup
        value={groupSelected}
        onChange={setGroupSelected}
        classNames={{
          base: "w-full",
        }}
      >
        {companies.map((c) => (
          <CustomCheckbox value={c.name} company={c} />
        ))}
      </CheckboxGroup>
      <p className="mt-4 ml-1 text-default-500">
        Selected: {groupSelected.join(", ")}
      </p>
    </div>
  );
}
