# TF::FortiOS::EndpointcontrolProfile ForticlientOperatingSystemDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#osname" title="OsName">OsName</a>" : <i>String</i>,
    "<a href="#ostype" title="OsType">OsType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#osname" title="OsName">OsName</a>: <i>String</i>
<a href="#ostype" title="OsType">OsType</a>: <i>String</i>
</pre>

## Properties

#### Id

Operating system entry ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsName

Customize operating system name or Mac OS format:x.x.x.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsType

Operating system type. Valid values: `custom`, `mac-os`, `win-7`, `win-80`, `win-81`, `win-10`, `win-2000`, `win-home-svr`, `win-svr-10`, `win-svr-2003`, `win-svr-2003-r2`, `win-svr-2008`, `win-svr-2008-r2`, `win-svr-2012`, `win-svr-2012-r2`, `win-sto-svr-2003`, `win-vista`, `win-xp`, `ubuntu-linux`, `centos-linux`, `redhat-linux`, `fedora-linux`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

