import { Avatar, Card, CardBody, Textarea } from "@nextui-org/react";

import { AIMessage } from "./AIMessage";
import { ASSISTANT } from "../../../constants/role";
import { LoadingMessage } from "../../Skeleton";
import React from "react";
import { UserMessage } from "./UserMessage";
import { useChatScroll } from "../../../hook/useChatScroll";

export function ListMessage({
  listMessage,
  usefulTable,
  getListMessage,
  getListUsefulMessage,
}) {
  const ref = useChatScroll(listMessage);

  return (
    <div className="flex flex-col overflow-auto p-4 h-full" ref={ref}>
      {listMessage.map((message, index) => (
        <div
          key={index}
          className={`max-w-1/2 ${
            message.role === ASSISTANT ? "self-start pr-4" : "self-end pl-4"
          }`}
        >
          {!(message.role === ASSISTANT) ? (
            <UserMessage message={message} />
          ) : (index === listMessage.length - 1 ||
              index === listMessage.length - 2) &&
            message.loading &&
            index != 0 ? (
            <div className="flex items-center">
              <Avatar
                className="h-8 w-8"
                isBordered
                radius="full"
                src="https://www.the-digital-insurer.com/wp-content/uploads/2016/06/718RobotFinance.jpg"
              />
              <Card className="mx-4">
                <CardBody className="py-4">
                  <LoadingMessage />
                </CardBody>
              </Card>
            </div>
          ) : (
            <AIMessage
              message={message}
              getListMessage={getListMessage}
              getListUsefulMessage={getListUsefulMessage}
            />
          )}
        </div>
      ))}
    </div>
  );
}
