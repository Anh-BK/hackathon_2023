import {
  AiFillCompass,
  AiFillSetting,
  AiOutlineClose,
  AiOutlineCloseCircle,
  AiOutlineTable,
} from "react-icons/ai";
import {
  Button,
  Modal,
  ModalBody,
  ModalContent,
  ModalFooter,
  ModalHeader,
  Tooltip,
  useDisclosure,
} from "@nextui-org/react";
import React, { useState } from "react";

import { CheckboxGroupCustom } from "./checkbox/CheckboxGroup";
import { TableAnswer } from "./Table";

const FloatingButton = ({ usefulTable }) => {
  const {
    isOpen: isOpenTable,
    onOpen: onOpenTable,
    onClose: onCloseTable,
  } = useDisclosure();

  const {
    isOpen: isOpenCompare,
    onOpen: onOpenCompare,
    onClose: onCloseCompare,
  } = useDisclosure();

  const {
    isOpen: isOpenPreviewCompare,
    onOpen: onOpenPreviewCompare,
    onClose: onClosePreviewCompare,
  } = useDisclosure();

  const [isOpen, setIsOpen] = useState(false);

  return (
    <>
      <Modal backdrop="blur" isOpen={isOpenTable} onClose={onCloseTable}>
        <ModalContent className="max-w-full">
          {(onClose) => (
            <>
              <ModalHeader className="flex flex-col gap-1">
                Modal Title
              </ModalHeader>
              <ModalBody>
                <div className="flex gap-x-2">
                  <TableAnswer usefulTable={usefulTable} />
                  <TableAnswer usefulTable={usefulTable} />
                </div>
              </ModalBody>
            </>
          )}
        </ModalContent>
      </Modal>

      <Modal backdrop="blur" isOpen={isOpenTable} onClose={onCloseTable}>
        <ModalContent className="max-w-full">
          {(onClose) => (
            <>
              <ModalHeader className="flex flex-col gap-1">
                Modal Title
              </ModalHeader>
              <ModalBody>
                <TableAnswer usefulTable={usefulTable} />
              </ModalBody>
            </>
          )}
        </ModalContent>
      </Modal>
      <Modal backdrop="blur" isOpen={isOpenTable} onClose={onCloseTable}>
        <ModalContent className="max-w-full">
          {(onClose) => (
            <>
              <ModalHeader className="flex flex-col gap-1">
                Modal Title
              </ModalHeader>
              <ModalBody>
                <TableAnswer usefulTable={usefulTable} />
              </ModalBody>
            </>
          )}
        </ModalContent>
      </Modal>
      <Modal backdrop="blur" isOpen={isOpenCompare} onClose={onCloseCompare}>
        <ModalContent>
          {(onClose) => (
            <>
              <ModalHeader className="flex flex-col gap-1">
                Select Companies
              </ModalHeader>
              <ModalBody>
                <CheckboxGroupCustom />
              </ModalBody>
              <ModalFooter>
                <Button color="danger" variant="light" onPress={onClose}>
                  Close
                </Button>
                <Button color="primary" onPress={onClose}>
                  Next
                </Button>
              </ModalFooter>
            </>
          )}
        </ModalContent>
      </Modal>
      <div className="fixed bottom-4 right-4">
        <div className="relative">
          <Button
            isIconOnly
            onClick={() => setIsOpen(!isOpen)}
            className="h-14 w-14"
          >
            {isOpen ? (
              <AiOutlineClose className="h-6 w-6" />
            ) : (
              <AiFillSetting className="h-6 w-6" />
            )}
          </Button>
          {isOpen ? (
            <>
              <div className="absolute top-[-70px]">
                <Tooltip
                  showArrow={true}
                  content="Open useful information table"
                >
                  <Button
                    isIconOnly
                    onClick={onOpenTable}
                    className="h-14 w-14"
                  >
                    <AiOutlineTable className="h-6 w-6" />
                  </Button>
                </Tooltip>
              </div>
              <div className="absolute right-[70px] top-0">
                <Tooltip
                  showArrow={true}
                  content="Compare companies"
                  placement="left-start"
                >
                  <Button
                    isIconOnly
                    onClick={onOpenCompare}
                    className="h-14 w-14"
                  >
                    <AiFillCompass className="h-6 w-6" />
                  </Button>
                </Tooltip>
              </div>
            </>
          ) : null}
        </div>
      </div>
    </>
  );
};

export default FloatingButton;
