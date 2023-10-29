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
import { columns, columnsPreview } from "../constants/table";

import { CheckboxGroupCustom } from "./checkbox/CheckboxGroup";
import Markdown from "react-markdown";
import { TableAnswer } from "./Table";
import axiosClient from "../config/axios";
import remarkGfm from "remark-gfm";

const FloatingButton = ({ usefulTable, getListUsefulMessage }) => {
  const [groupSelected, setGroupSelected] = React.useState([]);
  const [usefulTableFirstCompany, setUsefulTableFirstCompany] = useState([]);
  const [usefulTableSecondCompany, setUsefulTableSecondCompany] = useState([]);
  const [messageCompare, setMessageCompare] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const {
    isOpen: isOpenTable,
    onOpen: onOpenTable,
    onClose: onCloseTable,
  } = useDisclosure();

  const {
    isOpen: isOpenSelectCompare,
    onOpen: onOpenSelectCompare,
    onClose: onCloseSelectCompare,
  } = useDisclosure();

  const {
    isOpen: isOpenPreviewCompare,
    onOpen: onOpenPreviewCompare,
    onClose: onClosePreviewCompare,
  } = useDisclosure();

  const {
    isOpen: isOpenFinal,
    onOpen: onOpenFinal,
    onClose: onCloseFinal,
  } = useDisclosure();

  const [isOpen, setIsOpen] = useState(false);

  const handleCompare = async (company) => {
    const messages = await axiosClient.request({
      url: "/conversation/get_messages",
      method: "POST",
      data: {
        company_id: company,
        is_useful: true,
      },
    });

    const covertUsefulTable = messages.map((m, index) => ({
      id: m._id,
      answer: m.message,
      citations: m.citations,
    }));
    return covertUsefulTable;
  };

  const handlePreview = async () => {
    for (let i = 0; i < groupSelected.length; i++) {
      const response = await handleCompare(groupSelected[i]);
      if (i === 0) {
        setUsefulTableFirstCompany((prevState) => {
          return response;
        });
        continue;
      }
      setUsefulTableSecondCompany((prevState) => {
        return response;
      });
    }

    onCloseSelectCompare();
    onOpenPreviewCompare();
  };

  const onCompare = async () => {
    setIsLoading(true);
    const context1 = usefulTableFirstCompany.map((u) => u.answer).join("\\n");
    const context2 = usefulTableSecondCompany.map((u) => u.answer).join("\\n");

    const messages = await axiosClient.request({
      url: "/comparision/comparing",
      method: "POST",
      data: {
        context_1: context1,
        context_2: context2,
      },
    });
    setIsLoading(false);
    setMessageCompare(messages);
    onClosePreviewCompare();
    onOpenFinal();
  };

  return (
    <>
      <Modal backdrop="blur" isOpen={isOpenFinal} onClose={onCloseFinal}>
        <ModalContent className="max-w-full">
          {(onClose) => (
            <>
              <ModalHeader className="flex flex-col gap-x-2">
                Comparision
              </ModalHeader>
              <ModalBody>
                <Markdown
                  className="text-[14px] p-0"
                  remarkPlugins={[remarkGfm]}
                >
                  {messageCompare.content}
                </Markdown>
              </ModalBody>
              <ModalFooter>
                <Button
                  color="danger"
                  variant="light"
                  onPress={() => {
                    onCloseFinal();
                  }}
                >
                  Close
                </Button>
              </ModalFooter>
            </>
          )}
        </ModalContent>
      </Modal>

      <Modal
        backdrop="blur"
        isOpen={isOpenPreviewCompare}
        onClose={() => {
          onClosePreviewCompare();
        }}
      >
        <ModalContent className="max-w-full">
          {(onClose) => (
            <>
              <ModalHeader className="flex flex-col gap-x-2">
                Preview
              </ModalHeader>
              <ModalBody>
                <div className="flex gap-x-2">
                  <TableAnswer
                    columns={columnsPreview}
                    usefulTable={usefulTableFirstCompany}
                  />
                  <TableAnswer
                    columns={columnsPreview}
                    usefulTable={usefulTableSecondCompany}
                  />
                </div>
              </ModalBody>
              <ModalFooter>
                <Button
                  color="danger"
                  variant="light"
                  onPress={() => {
                    onClosePreviewCompare();
                  }}
                >
                  Close
                </Button>
                <Button
                  color="primary"
                  onPress={onCompare}
                  isLoading={isLoading}
                >
                  Compare
                </Button>
              </ModalFooter>
            </>
          )}
        </ModalContent>
      </Modal>

      <Modal
        backdrop="blur"
        isOpen={isOpenSelectCompare}
        onClose={onCloseSelectCompare}
      >
        <ModalContent>
          {(onClose) => (
            <>
              <ModalHeader className="flex flex-col gap-1">
                Select Companies
              </ModalHeader>
              <ModalBody>
                <CheckboxGroupCustom
                  groupSelected={groupSelected}
                  setGroupSelected={setGroupSelected}
                />
              </ModalBody>
              <ModalFooter>
                <Button
                  color="danger"
                  variant="light"
                  onPress={onCloseSelectCompare}
                >
                  Close
                </Button>
                <Button color="primary" onPress={handlePreview}>
                  Next
                </Button>
              </ModalFooter>
            </>
          )}
        </ModalContent>
      </Modal>

      <Modal backdrop="blur" isOpen={isOpenTable} onClose={onCloseTable}>
        <ModalContent className="max-w-full">
          {(onClose) => (
            <>
              <ModalHeader className="flex flex-col gap-1">Table</ModalHeader>
              <ModalBody>
                <TableAnswer
                  columns={columns}
                  usefulTable={usefulTable}
                  getListUsefulMessage={getListUsefulMessage}
                />
              </ModalBody>
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
                    onClick={onOpenSelectCompare}
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
