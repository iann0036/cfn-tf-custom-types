# TF::FortiOS::DlpSensor FilterDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#archive" title="Archive">Archive</a>" : <i>String</i>,
    "<a href="#companyidentifier" title="CompanyIdentifier">CompanyIdentifier</a>" : <i>String</i>,
    "<a href="#expiry" title="Expiry">Expiry</a>" : <i>String</i>,
    "<a href="#filesize" title="FileSize">FileSize</a>" : <i>Double</i>,
    "<a href="#filetype" title="FileType">FileType</a>" : <i>Double</i>,
    "<a href="#filterby" title="FilterBy">FilterBy</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#matchpercentage" title="MatchPercentage">MatchPercentage</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#proto" title="Proto">Proto</a>" : <i>String</i>,
    "<a href="#regexp" title="Regexp">Regexp</a>" : <i>String</i>,
    "<a href="#severity" title="Severity">Severity</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#fpsensitivity" title="FpSensitivity">FpSensitivity</a>" : <i>[ <a href="fpsensitivitydefinition.md">FpSensitivityDefinition</a>, ... ]</i>,
    "<a href="#sensitivity" title="Sensitivity">Sensitivity</a>" : <i>[ <a href="sensitivitydefinition.md">SensitivityDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#archive" title="Archive">Archive</a>: <i>String</i>
<a href="#companyidentifier" title="CompanyIdentifier">CompanyIdentifier</a>: <i>String</i>
<a href="#expiry" title="Expiry">Expiry</a>: <i>String</i>
<a href="#filesize" title="FileSize">FileSize</a>: <i>Double</i>
<a href="#filetype" title="FileType">FileType</a>: <i>Double</i>
<a href="#filterby" title="FilterBy">FilterBy</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#matchpercentage" title="MatchPercentage">MatchPercentage</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#proto" title="Proto">Proto</a>: <i>String</i>
<a href="#regexp" title="Regexp">Regexp</a>: <i>String</i>
<a href="#severity" title="Severity">Severity</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#fpsensitivity" title="FpSensitivity">FpSensitivity</a>: <i>
      - <a href="fpsensitivitydefinition.md">FpSensitivityDefinition</a></i>
<a href="#sensitivity" title="Sensitivity">Sensitivity</a>: <i>
      - <a href="sensitivitydefinition.md">SensitivityDefinition</a></i>
</pre>

## Properties

#### Action

Action to take with content that this DLP sensor matches. Valid values: `allow`, `log-only`, `block`, `quarantine-ip`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Archive

Enable/disable DLP archiving. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompanyIdentifier

Enter a company identifier watermark to match. Only watermarks that your company has placed on the files are matched.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expiry

Quarantine duration in days, hours, minutes format (dddhhmm).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileSize

Match files this size or larger (0 - 4294967295 kbytes).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileType

Select the number of a DLP file pattern table to match.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterBy

Select the type of content to match. Valid values: `credit-card`, `ssn`, `regexp`, `file-type`, `file-size`, `fingerprint`, `watermark`, `encrypted`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchPercentage

Percentage of fingerprints in the fingerprint databases designated with the selected fp-sensitivity to match.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Filter name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Proto

Check messages or files over one or more of these protocols.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Regexp

Enter a regular expression to match (max. 255 characters).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Severity

Select the severity or threat level that matches this filter. Valid values: `info`, `low`, `medium`, `high`, `critical`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Select whether to check the content of messages (an email message) or files (downloaded files or email attachments).  Valid values: `file`, `message`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FpSensitivity

_Required_: No

_Type_: List of <a href="fpsensitivitydefinition.md">FpSensitivityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sensitivity

_Required_: No

_Type_: List of <a href="sensitivitydefinition.md">SensitivityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

