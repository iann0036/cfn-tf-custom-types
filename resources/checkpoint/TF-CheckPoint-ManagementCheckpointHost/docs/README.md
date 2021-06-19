# TF::CheckPoint::ManagementCheckpointHost

This resource allows you to execute Check Point Checkpoint Host.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CheckPoint::ManagementCheckpointHost",
    "Properties" : {
        "<a href="#color" title="Color">Color</a>" : <i>String</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#hardware" title="Hardware">Hardware</a>" : <i>String</i>,
        "<a href="#ignoreerrors" title="IgnoreErrors">IgnoreErrors</a>" : <i>Boolean</i>,
        "<a href="#ignorewarnings" title="IgnoreWarnings">IgnoreWarnings</a>" : <i>Boolean</i>,
        "<a href="#ipv4address" title="Ipv4Address">Ipv4Address</a>" : <i>String</i>,
        "<a href="#ipv6address" title="Ipv6Address">Ipv6Address</a>" : <i>String</i>,
        "<a href="#logssettings" title="LogsSettings">LogsSettings</a>" : <i>[ <a href="logssettingsdefinition.md">LogsSettingsDefinition</a>, ... ]</i>,
        "<a href="#managementblades" title="ManagementBlades">ManagementBlades</a>" : <i>[ <a href="managementbladesdefinition.md">ManagementBladesDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#natsettings" title="NatSettings">NatSettings</a>" : <i>[ <a href="natsettingsdefinition.md">NatSettingsDefinition</a>, ... ]</i>,
        "<a href="#onetimepassword" title="OneTimePassword">OneTimePassword</a>" : <i>String</i>,
        "<a href="#os" title="Os">Os</a>" : <i>String</i>,
        "<a href="#savelogslocally" title="SaveLogsLocally">SaveLogsLocally</a>" : <i>Boolean</i>,
        "<a href="#sendalertstoserver" title="SendAlertsToServer">SendAlertsToServer</a>" : <i>[ String, ... ]</i>,
        "<a href="#sendlogstobackupserver" title="SendLogsToBackupServer">SendLogsToBackupServer</a>" : <i>[ String, ... ]</i>,
        "<a href="#sendlogstoserver" title="SendLogsToServer">SendLogsToServer</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#interfaces" title="Interfaces">Interfaces</a>" : <i>[ <a href="interfacesdefinition.md">InterfacesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CheckPoint::ManagementCheckpointHost
Properties:
    <a href="#color" title="Color">Color</a>: <i>String</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#hardware" title="Hardware">Hardware</a>: <i>String</i>
    <a href="#ignoreerrors" title="IgnoreErrors">IgnoreErrors</a>: <i>Boolean</i>
    <a href="#ignorewarnings" title="IgnoreWarnings">IgnoreWarnings</a>: <i>Boolean</i>
    <a href="#ipv4address" title="Ipv4Address">Ipv4Address</a>: <i>String</i>
    <a href="#ipv6address" title="Ipv6Address">Ipv6Address</a>: <i>String</i>
    <a href="#logssettings" title="LogsSettings">LogsSettings</a>: <i>
      - <a href="logssettingsdefinition.md">LogsSettingsDefinition</a></i>
    <a href="#managementblades" title="ManagementBlades">ManagementBlades</a>: <i>
      - <a href="managementbladesdefinition.md">ManagementBladesDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#natsettings" title="NatSettings">NatSettings</a>: <i>
      - <a href="natsettingsdefinition.md">NatSettingsDefinition</a></i>
    <a href="#onetimepassword" title="OneTimePassword">OneTimePassword</a>: <i>String</i>
    <a href="#os" title="Os">Os</a>: <i>String</i>
    <a href="#savelogslocally" title="SaveLogsLocally">SaveLogsLocally</a>: <i>Boolean</i>
    <a href="#sendalertstoserver" title="SendAlertsToServer">SendAlertsToServer</a>: <i>
      - String</i>
    <a href="#sendlogstobackupserver" title="SendLogsToBackupServer">SendLogsToBackupServer</a>: <i>
      - String</i>
    <a href="#sendlogstoserver" title="SendLogsToServer">SendLogsToServer</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#interfaces" title="Interfaces">Interfaces</a>: <i>
      - <a href="interfacesdefinition.md">InterfacesDefinition</a></i>
</pre>

## Properties

#### Color

Color of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

Comments string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hardware

Hardware name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreErrors

Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreWarnings

Apply changes ignoring warnings.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4Address

IPv4 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Address

IPv6 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogsSettings

Logs settings. logs_settings blocks are documented below.

_Required_: No

_Type_: List of <a href="logssettingsdefinition.md">LogsSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagementBlades

Management blades. management_blades blocks are documented below.

_Required_: No

_Type_: List of <a href="managementbladesdefinition.md">ManagementBladesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Object name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NatSettings

NAT settings. nat_settings blocks are documented below.

_Required_: No

_Type_: List of <a href="natsettingsdefinition.md">NatSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OneTimePassword

Secure internal connection one time password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Os

Operating system name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SaveLogsLocally

Enable save logs locally.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendAlertsToServer

Collection of Server(s) to send alerts to identified by the name or UID.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendLogsToBackupServer

Collection of Backup server(s) to send logs to identified by the name or UID.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendLogsToServer

Collection of Server(s) to send logs to identified by the name or UID.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Collection of tag identifiers.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

Checkpoint host platform version.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interfaces

_Required_: No

_Type_: List of <a href="interfacesdefinition.md">InterfacesDefinition</a>

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

#### SicName

Name of the Secure Internal Connection Trust.

#### SicState

State the Secure Internal Connection Trust.

