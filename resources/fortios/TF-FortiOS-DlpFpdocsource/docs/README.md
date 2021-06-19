# TF::FortiOS::DlpFpdocsource

Create a DLP fingerprint database by allowing the FortiGate to access a file server containing files from which to create fingerprints.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::DlpFpdocsource",
    "Properties" : {
        "<a href="#date" title="Date">Date</a>" : <i>Double</i>,
        "<a href="#filepath" title="FilePath">FilePath</a>" : <i>String</i>,
        "<a href="#filepattern" title="FilePattern">FilePattern</a>" : <i>String</i>,
        "<a href="#keepmodified" title="KeepModified">KeepModified</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#period" title="Period">Period</a>" : <i>String</i>,
        "<a href="#removedeleted" title="RemoveDeleted">RemoveDeleted</a>" : <i>String</i>,
        "<a href="#scanoncreation" title="ScanOnCreation">ScanOnCreation</a>" : <i>String</i>,
        "<a href="#scansubdirectories" title="ScanSubdirectories">ScanSubdirectories</a>" : <i>String</i>,
        "<a href="#sensitivity" title="Sensitivity">Sensitivity</a>" : <i>String</i>,
        "<a href="#server" title="Server">Server</a>" : <i>String</i>,
        "<a href="#servertype" title="ServerType">ServerType</a>" : <i>String</i>,
        "<a href="#todhour" title="TodHour">TodHour</a>" : <i>Double</i>,
        "<a href="#todmin" title="TodMin">TodMin</a>" : <i>Double</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>,
        "<a href="#vdom" title="Vdom">Vdom</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#weekday" title="Weekday">Weekday</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::DlpFpdocsource
Properties:
    <a href="#date" title="Date">Date</a>: <i>Double</i>
    <a href="#filepath" title="FilePath">FilePath</a>: <i>String</i>
    <a href="#filepattern" title="FilePattern">FilePattern</a>: <i>String</i>
    <a href="#keepmodified" title="KeepModified">KeepModified</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#period" title="Period">Period</a>: <i>String</i>
    <a href="#removedeleted" title="RemoveDeleted">RemoveDeleted</a>: <i>String</i>
    <a href="#scanoncreation" title="ScanOnCreation">ScanOnCreation</a>: <i>String</i>
    <a href="#scansubdirectories" title="ScanSubdirectories">ScanSubdirectories</a>: <i>String</i>
    <a href="#sensitivity" title="Sensitivity">Sensitivity</a>: <i>String</i>
    <a href="#server" title="Server">Server</a>: <i>String</i>
    <a href="#servertype" title="ServerType">ServerType</a>: <i>String</i>
    <a href="#todhour" title="TodHour">TodHour</a>: <i>Double</i>
    <a href="#todmin" title="TodMin">TodMin</a>: <i>Double</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
    <a href="#vdom" title="Vdom">Vdom</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#weekday" title="Weekday">Weekday</a>: <i>String</i>
</pre>

## Properties

#### Date

Day of the month on which to scan the server (1 - 31).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilePath

Path on the server to the fingerprint files (max 119 characters).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilePattern

Files matching this pattern on the server are fingerprinted. Optionally use the * and ? wildcards.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepModified

Enable so that when a file is changed on the server the FortiGate keeps the old fingerprint and adds a new fingerprint to the database. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the DLP fingerprint database.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Password required to log into the file server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

Frequency for which the FortiGate checks the server for new or changed files. Valid values: `none`, `daily`, `weekly`, `monthly`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoveDeleted

Enable to keep the fingerprint database up to date when a file is deleted from the server. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScanOnCreation

Enable to keep the fingerprint database up to date when a file is added or changed on the server. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScanSubdirectories

Enable/disable scanning subdirectories to find files to create fingerprints from. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sensitivity

Select a sensitivity or threat level for matches with this fingerprint database. Add sensitivities using fp-sensitivity.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Server

IPv4 or IPv6 address of the server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerType

Protocol used to communicate with the file server. Currently only Samba (SMB) servers are supported. Valid values: `samba`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TodHour

Hour of the day on which to scan the server (0 - 23, default = 1).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TodMin

Minute of the hour on which to scan the server (0 - 59).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

User name required to log into the file server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdom

Select the VDOM that can communicate with the file server. Valid values: `mgmt`, `current`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weekday

Day of the week on which to scan the server. Valid values: `sunday`, `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday`.

_Required_: No

_Type_: String

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

