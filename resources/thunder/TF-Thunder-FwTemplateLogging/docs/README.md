# TF::Thunder::FwTemplateLogging

`thunder_fw_template_logging` Provides details about thunder fw template logging

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::FwTemplateLogging",
    "Properties" : {
        "<a href="#facility" title="Facility">Facility</a>" : <i>String</i>,
        "<a href="#format" title="Format">Format</a>" : <i>String</i>,
        "<a href="#includedestfqdn" title="IncludeDestFqdn">IncludeDestFqdn</a>" : <i>Double</i>,
        "<a href="#mergedstyle" title="MergedStyle">MergedStyle</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resolution" title="Resolution">Resolution</a>" : <i>String</i>,
        "<a href="#servicegroup" title="ServiceGroup">ServiceGroup</a>" : <i>String</i>,
        "<a href="#severity" title="Severity">Severity</a>" : <i>String</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#includehttp" title="IncludeHttp">IncludeHttp</a>" : <i>[ <a href="includehttpdefinition.md">IncludeHttpDefinition</a>, ... ]</i>,
        "<a href="#includeradiusattribute" title="IncludeRadiusAttribute">IncludeRadiusAttribute</a>" : <i>[ <a href="includeradiusattributedefinition.md">IncludeRadiusAttributeDefinition</a>, ... ]</i>,
        "<a href="#log" title="Log">Log</a>" : <i>[ <a href="logdefinition.md">LogDefinition</a>, ... ]</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="ruledefinition.md">RuleDefinition</a>, ... ]</i>,
        "<a href="#sourceaddress" title="SourceAddress">SourceAddress</a>" : <i>[ <a href="sourceaddressdefinition.md">SourceAddressDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::FwTemplateLogging
Properties:
    <a href="#facility" title="Facility">Facility</a>: <i>String</i>
    <a href="#format" title="Format">Format</a>: <i>String</i>
    <a href="#includedestfqdn" title="IncludeDestFqdn">IncludeDestFqdn</a>: <i>Double</i>
    <a href="#mergedstyle" title="MergedStyle">MergedStyle</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resolution" title="Resolution">Resolution</a>: <i>String</i>
    <a href="#servicegroup" title="ServiceGroup">ServiceGroup</a>: <i>String</i>
    <a href="#severity" title="Severity">Severity</a>: <i>String</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#includehttp" title="IncludeHttp">IncludeHttp</a>: <i>
      - <a href="includehttpdefinition.md">IncludeHttpDefinition</a></i>
    <a href="#includeradiusattribute" title="IncludeRadiusAttribute">IncludeRadiusAttribute</a>: <i>
      - <a href="includeradiusattributedefinition.md">IncludeRadiusAttributeDefinition</a></i>
    <a href="#log" title="Log">Log</a>: <i>
      - <a href="logdefinition.md">LogDefinition</a></i>
    <a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="ruledefinition.md">RuleDefinition</a></i>
    <a href="#sourceaddress" title="SourceAddress">SourceAddress</a>: <i>
      - <a href="sourceaddressdefinition.md">SourceAddressDefinition</a></i>
</pre>

## Properties

#### Facility

‘kernel’: 0: Kernel; ‘user’: 1: User-level; ‘mail’: 2: Mail; ‘daemon’: 3: System daemons; ‘security-authorization’: 4: Security/authorization; ‘syslog’: 5: Syslog internal; ‘line-printer’: 6: Line printer; ‘news’: 7: Network news; ‘uucp’: 8: UUCP subsystem; ‘cron’: 9: Time-related; ‘security-authorization-private’: 10: Private security/authorization; ‘ftp’: 11: FTP; ‘ntp’: 12: NTP; ‘audit’: 13: Audit; ‘alert’: 14: Alert; ‘clock’: 15: Clock-related; ‘local0’: 16: Local use 0; ‘local1’: 17: Local use 1; ‘local2’: 18: Local use 2; ‘local3’: 19: Local use 3; ‘local4’: 20: Local use 4; ‘local5’: 21: Local use 5; ‘local6’: 22: Local use 6; ‘local7’: 23: Local use 7;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Format

‘ascii’: A10 Text logging format (ASCII); ‘cef’: Common Event Format for logging (default);.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeDestFqdn

Include destination FQDN string.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MergedStyle

Merge creation and deletion of session logs to one.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Logging Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resolution

‘seconds’: Logging timestamp resolution in seconds (default); ‘10-milliseconds’: Logging timestamp resolution in 10s of milli-seconds;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceGroup

Bind a Service Group to the logging template (Service Group Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Severity

‘emergency’: 0: Emergency; ‘alert’: 1: Alert; ‘critical’: 2: Critical; ‘error’: 3: Error; ‘warning’: 4: Warning; ‘notice’: 5: Notice; ‘informational’: 6: Informational; ‘debug’: 7: Debug;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

Customized tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeHttp

_Required_: No

_Type_: List of <a href="includehttpdefinition.md">IncludeHttpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeRadiusAttribute

_Required_: No

_Type_: List of <a href="includeradiusattributedefinition.md">IncludeRadiusAttributeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Log

_Required_: No

_Type_: List of <a href="logdefinition.md">LogDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of <a href="ruledefinition.md">RuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAddress

_Required_: No

_Type_: List of <a href="sourceaddressdefinition.md">SourceAddressDefinition</a>

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

