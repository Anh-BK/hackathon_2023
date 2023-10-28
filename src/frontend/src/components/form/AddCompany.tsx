import {
  Button,
  Checkbox,
  Input,
  Link,
  Modal,
  ModalBody,
  ModalContent,
  ModalFooter,
  ModalHeader,
  useDisclosure,
} from "@nextui-org/react";
import { addCompany, companies } from "../../constants/company";

import React from "react";

export function AddCompany({
  isOpen,
  onOpen,
  onClose,
  onOpenChange,
  setListCompany,
  setCompany,
}) {
  const onSubmit = () => {
    const newListCompany = [...companies, addCompany];
    setListCompany(newListCompany);
    setCompany(addCompany.id);
    onClose();
  };

  return (
    <Modal
      backdrop="blur"
      isOpen={isOpen}
      onOpenChange={onOpenChange}
      placement="top-center"
    >
      <ModalContent>
        {() => (
          <>
            <ModalHeader className="flex flex-col gap-1">
              Add Company
            </ModalHeader>
            <ModalBody>
              <Input type="name" variant="flat" label="Name of company" />
            </ModalBody>
            <ModalFooter>
              <Button color="danger" variant="light" onPress={onClose}>
                Close
              </Button>
              <Button color="primary" onPress={onSubmit}>
                Add
              </Button>
            </ModalFooter>
          </>
        )}
      </ModalContent>
    </Modal>
  );
}
