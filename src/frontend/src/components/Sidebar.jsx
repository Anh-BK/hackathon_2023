import { Menu, MenuItem, Sidebar, menuClasses } from "react-pro-sidebar";

import React from "react";

const themes = {
  dark: {
    sidebar: {
      backgroundColor: "#0b2948",
      color: "#8ba1b7",
    },
    menu: {
      menuContent: "#082440",
      icon: "#59d0ff",
      hover: {
        backgroundColor: "#00458b",
        color: "#b6c8d9",
      },
      disabled: {
        color: "#3e5e7e",
      },
    },
  },
};

// hex to rgba converter
const hexToRgba = (hex, alpha) => {
  const r = parseInt(hex.slice(1, 3), 16);
  const g = parseInt(hex.slice(3, 5), 16);
  const b = parseInt(hex.slice(5, 7), 16);

  return `rgba(${r}, ${g}, ${b}, ${alpha})`;
};

export const SidebarCustom = () => {
  const [collapsed, setCollapsed] = React.useState(false);
  const [toggled, setToggled] = React.useState(false);

  const menuItemStyles = {
    root: {
      fontSize: "13px",
      fontWeight: 400,
    },
    icon: {
      color: themes["dark"].menu.icon,
      [`&.${menuClasses.disabled}`]: {
        color: themes["dark"].menu.disabled.color,
      },
    },
    SubMenuExpandIcon: {
      color: "#b6b7b9",
    },
    subMenuContent: ({ level }) => ({
      backgroundColor:
        level === 0
          ? hexToRgba(themes["dark"].menu.menuContent, 1)
          : "transparent",
    }),
    button: {
      [`&.${menuClasses.disabled}`]: {
        color: themes["dark"].menu.disabled.color,
      },
      "&:hover": {
        backgroundColor: hexToRgba(
          themes["dark"].menu.hover.backgroundColor,
          1
        ),
        color: themes["dark"].menu.hover.color,
      },
    },
    label: ({ open }) => ({
      fontWeight: open ? 600 : undefined,
    }),
  };

  return (
    <Sidebar
      collapsed={collapsed}
      toggled={toggled}
      onBackdropClick={() => setToggled(false)}
      image="https://user-images.githubusercontent.com/25878302/144499035-2911184c-76d3-4611-86e7-bc4e8ff84ff5.jpg"
      breakPoint="md"
      backgroundColor={hexToRgba(themes["dark"].sidebar.backgroundColor, 1)}
      rootStyles={{
        color: themes["dark"].sidebar.color,
      }}
    >
      <div style={{ display: "flex", flexDirection: "column", height: "100%" }}>
        {/* <SidebarHeader style={{ marginBottom: "24px", marginTop: "16px" }} /> */}
        <div style={{ flex: 1, marginBottom: "32px" }}>
          <Menu menuItemStyles={menuItemStyles}>
            <MenuItem>Calendar</MenuItem>
            <MenuItem>Documentation</MenuItem>
            <MenuItem disabled>Examples</MenuItem>
          </Menu>
        </div>
        {/* <SidebarFooter collapsed={collapsed} /> */}
      </div>
    </Sidebar>
  );
};
