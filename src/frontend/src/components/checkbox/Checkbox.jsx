import { Checkbox, Chip, Image, Link, User, cn } from "@nextui-org/react";

import React from "react";

export const CustomCheckbox = ({ company, value }) => {
  return (
    <Checkbox
      aria-label={company.name}
      classNames={{
        base: cn(
          "inline-flex max-w-md w-full bg-content1 m-0",
          "hover:bg-content2 items-center justify-start",
          "cursor-pointer rounded-lg gap-2 p-4 border-2 border-transparent",
          "data-[selected=true]:border-primary"
        ),
        label: "w-full",
      }}
      value={value}
    >
      <div className="flex gap-x-4 items-center">
        <Image src={company.logoURL} width={20} height={20} />
        <p>{company.name}</p>
      </div>
    </Checkbox>
  );
};
