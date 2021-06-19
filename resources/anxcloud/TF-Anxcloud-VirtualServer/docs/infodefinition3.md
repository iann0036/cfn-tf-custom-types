# TF::Anxcloud::VirtualServer InfoDefinition3

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cores" title="Cores">Cores</a>" : <i>Double</i>,
    "<a href="#cpu" title="Cpu">Cpu</a>" : <i>Double</i>,
    "<a href="#customname" title="CustomName">CustomName</a>" : <i>String</i>,
    "<a href="#disksinfo" title="DisksInfo">DisksInfo</a>" : <i>[ <a href="infodefinition.md">InfoDefinition</a>, ... ]</i>,
    "<a href="#disksnumber" title="DisksNumber">DisksNumber</a>" : <i>Double</i>,
    "<a href="#guestos" title="GuestOs">GuestOs</a>" : <i>String</i>,
    "<a href="#guesttoolsstatus" title="GuestToolsStatus">GuestToolsStatus</a>" : <i>String</i>,
    "<a href="#identifier" title="Identifier">Identifier</a>" : <i>String</i>,
    "<a href="#locationcode" title="LocationCode">LocationCode</a>" : <i>String</i>,
    "<a href="#locationcountry" title="LocationCountry">LocationCountry</a>" : <i>String</i>,
    "<a href="#locationname" title="LocationName">LocationName</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#network" title="Network">Network</a>" : <i>[ <a href="infodefinition2.md">InfoDefinition2</a>, ... ]</i>,
    "<a href="#ram" title="Ram">Ram</a>" : <i>Double</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#versiontools" title="VersionTools">VersionTools</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#cores" title="Cores">Cores</a>: <i>Double</i>
<a href="#cpu" title="Cpu">Cpu</a>: <i>Double</i>
<a href="#customname" title="CustomName">CustomName</a>: <i>String</i>
<a href="#disksinfo" title="DisksInfo">DisksInfo</a>: <i>
      - <a href="infodefinition.md">InfoDefinition</a></i>
<a href="#disksnumber" title="DisksNumber">DisksNumber</a>: <i>Double</i>
<a href="#guestos" title="GuestOs">GuestOs</a>: <i>String</i>
<a href="#guesttoolsstatus" title="GuestToolsStatus">GuestToolsStatus</a>: <i>String</i>
<a href="#identifier" title="Identifier">Identifier</a>: <i>String</i>
<a href="#locationcode" title="LocationCode">LocationCode</a>: <i>String</i>
<a href="#locationcountry" title="LocationCountry">LocationCountry</a>: <i>String</i>
<a href="#locationname" title="LocationName">LocationName</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#network" title="Network">Network</a>: <i>
      - <a href="infodefinition2.md">InfoDefinition2</a></i>
<a href="#ram" title="Ram">Ram</a>: <i>Double</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#versiontools" title="VersionTools">VersionTools</a>: <i>String</i>
</pre>

## Properties

#### Cores

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cpu

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisksInfo

_Required_: No

_Type_: List of <a href="infodefinition.md">InfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisksNumber

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestOs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestToolsStatus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identifier

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocationCode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocationCountry

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocationName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: List of <a href="infodefinition2.md">InfoDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ram

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionTools

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

