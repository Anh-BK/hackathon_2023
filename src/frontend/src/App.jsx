import {
  Avatar,
  Button,
  Card,
  CardBody,
  CardFooter,
  Select,
  SelectItem,
} from "@nextui-org/react";
import { Menu, MenuItem, Sidebar, SubMenu } from "react-pro-sidebar";
import React, { useEffect, useState } from "react";

import { BoxChat } from "./components/chat/BoxChat";
import FloatingButton from "./components/FAB";
import { HeaderCompany } from "./components/Header";
import { ListMessage } from "./components/chat/message/ListMessage";
import { MdAddToPhotos } from "react-icons/md";
import { SidebarCustom } from "./components/Sidebar";
import { SwitchAction } from "./components/SwitchAction";
import { TableAnswer } from "./components/Table";
import axiosClient from "./config/axios";
import { companies } from "./constants/company";
import { predefineAction } from "./constants/predefineAction";

export default function App() {
  const [company, setCompany] = useState(companies[0].name);
  const [preAction, setPreAction] = useState(null);
  const [usefulTable, setUsefulTable] = useState([]);
  const [listMessage, setListMessage] = useState([]);

  const getListMessage = async () => {
    const messages = await axiosClient.request({
      url: "/conversation/get_messages",
      method: "POST",
      data: {
        company_id: company,
      },
    });
    setListMessage(messages);
  };

  const getListUsefulMessage = async () => {
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
    setUsefulTable(covertUsefulTable);
  };

  useEffect(() => {
    getListMessage();
    getListUsefulMessage();
  }, [company]);

  return (
    <div className="bg-color flex max-h-screen min-h-screen">
      <div className="flex-1 p-6">
        <div className="flex justify-center">
          <HeaderCompany
            className="w-1/2"
            setCompany={setCompany}
            company={company}
          />
        </div>
        <div className="mt-10 w-full flex justify-between h-[75%]">
          <div className="w-[80%]">
            <ListMessage
              listMessage={listMessage}
              getListMessage={getListMessage}
              usefulTable={usefulTable}
              getListUsefulMessage={getListUsefulMessage}
            />
            <BoxChat
              preAction={preAction}
              company={company}
              listMessage={listMessage}
              setListMessage={setListMessage}
            />
          </div>
          <div className="w-[20%] ml-10 flex flex-col gap-y-4">
            {predefineAction.map((action) => (
              <SwitchAction
                preAction={preAction}
                setPreAction={setPreAction}
                id={action.id}
                name={action.title}
                defaultSelected={action.defaultSelected}
                valueAction={action.value}
              />
            ))}
          </div>
        </div>
        <FloatingButton
          getListUsefulMessage={getListUsefulMessage}
          usefulTable={usefulTable}
          setUsefulTable={setUsefulTable}
        />
      </div>
    </div>
  );
}
