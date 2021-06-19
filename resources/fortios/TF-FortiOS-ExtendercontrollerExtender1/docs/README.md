# TF::FortiOS::ExtendercontrollerExtender1

Extender controller configuration.

-> The resource applies to FortiOS Version >= 6.4.2. For FortiOS Version < 6.4.2, see `fortios_extendercontroller_extender`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::ExtendercontrollerExtender1",
    "Properties" : {
        "<a href="#authorized" title="Authorized">Authorized</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#extname" title="ExtName">ExtName</a>" : <i>String</i>,
        "<a href="#fosid" title="Fosid">Fosid</a>" : <i>String</i>,
        "<a href="#loginpassword" title="LoginPassword">LoginPassword</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#vdom" title="Vdom">Vdom</a>" : <i>Double</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#controllerreport" title="ControllerReport">ControllerReport</a>" : <i>[ <a href="controllerreportdefinition.md">ControllerReportDefinition</a>, ... ]</i>,
        "<a href="#modem1" title="Modem1">Modem1</a>" : <i>[ <a href="modem1definition.md">Modem1Definition</a>, ... ]</i>,
        "<a href="#modem2" title="Modem2">Modem2</a>" : <i>[ <a href="modem2definition.md">Modem2Definition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::ExtendercontrollerExtender1
Properties:
    <a href="#authorized" title="Authorized">Authorized</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#extname" title="ExtName">ExtName</a>: <i>String</i>
    <a href="#fosid" title="Fosid">Fosid</a>: <i>String</i>
    <a href="#loginpassword" title="LoginPassword">LoginPassword</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#vdom" title="Vdom">Vdom</a>: <i>Double</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#controllerreport" title="ControllerReport">ControllerReport</a>: <i>
      - <a href="controllerreportdefinition.md">ControllerReportDefinition</a></i>
    <a href="#modem1" title="Modem1">Modem1</a>: <i>
      - <a href="modem1definition.md">Modem1Definition</a></i>
    <a href="#modem2" title="Modem2">Modem2</a>: <i>
      - <a href="modem2definition.md">Modem2Definition</a></i>
</pre>

## Properties

#### Authorized

FortiExtender Administration (enable or disable). Valid values: `disable`, `enable`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtName

FortiExtender name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fosid

FortiExtender serial number.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoginPassword

FortiExtender login password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

FortiExtender entry name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdom

VDOM.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControllerReport

_Required_: No

_Type_: List of <a href="controllerreportdefinition.md">ControllerReportDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Modem1

_Required_: No

_Type_: List of <a href="modem1definition.md">Modem1Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Modem2

_Required_: No

_Type_: List of <a href="modem2definition.md">Modem2Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

