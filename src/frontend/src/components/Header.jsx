import {
  Card,
  CardBody,
  CardHeader,
  Image,
  Select,
  SelectItem,
  useDisclosure,
} from "@nextui-org/react";
import React, { useState } from "react";

import { AddCompany } from "./form/AddCompany";
import { BsBuildingAdd } from "react-icons/bs";
import { companies } from "../constants/company";

const ADD_COMPANY_OPTION = {
  id: "add_company",
};

export function HeaderCompany({ className, setCompany, company }) {
  const { isOpen, onOpen, onOpenChange, onClose } = useDisclosure();
  const [listCompany, setListCompany] = useState(companies);

  const onChange = (e) => {
    // if (e.target.value === ADD_COMPANY_OPTION.id) {
    //   onOpen();
    //   return;
    // }
    setCompany(e.target.value);
  };

  return (
    <>
      <AddCompany
        isOpen={isOpen}
        onOpen={onOpen}
        onOpenChange={onOpenChange}
        onClose={onClose}
        setListCompany={setListCompany}
        setCompany={setCompany}
      />
      <Select
        onChange={onChange}
        items={[...listCompany]}
        label="Select company"
        className={className}
        defaultSelectedKeys={[listCompany[0].name]}
        renderValue={(items) => {
          return items.map((item) => {
            // if (item.data.id === ADD_COMPANY_OPTION.id) {
            //   return null;
            // }
            return (
              <div className="flex gap-x-4 items-center" key={item.data.id}>
                <Image src={item.data.logoURL} width={20} height={20} />
                <p>{item.data.name}</p>
              </div>
            );
          });
        }}
      >
        {(company) => {
          // if (company.id === ADD_COMPANY_OPTION.id) {
          //   return (
          //     <SelectItem
          //       key={company.id}
          //       textValue={company.id}
          //       value={company.id}
          //     >
          //       <div className="flex gap-x-4 items-center justify-center">
          //         <BsBuildingAdd />
          //         <p>Add Company</p>
          //       </div>
          //     </SelectItem>
          //   );
          // }
          return (
            <SelectItem
              key={company.name}
              textValue={company.name}
              value={company.name}
            >
              <div className="flex gap-x-4 items-center">
                <Image src={company.logoURL} width={20} height={20} />
                <p>{company.name}</p>
              </div>
            </SelectItem>
          );
        }}
      </Select>
    </>
  );
}
