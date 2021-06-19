# TF::SumoLogic::S3AuditSource

CloudFormation equivalent of sumologic_s3_audit_source

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::SumoLogic::S3AuditSource",
    "Properties" : {
        "<a href="#automaticdateparsing" title="AutomaticDateParsing">AutomaticDateParsing</a>" : <i>Boolean</i>,
        "<a href="#category" title="Category">Category</a>" : <i>String</i>,
        "<a href="#collectorid" title="CollectorId">CollectorId</a>" : <i>Double</i>,
        "<a href="#contenttype" title="ContentType">ContentType</a>" : <i>String</i>,
        "<a href="#cutoffrelativetime" title="CutoffRelativeTime">CutoffRelativeTime</a>" : <i>String</i>,
        "<a href="#cutofftimestamp" title="CutoffTimestamp">CutoffTimestamp</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#fields" title="Fields">Fields</a>" : <i>[ <a href="fieldsdefinition.md">FieldsDefinition</a>, ... ]</i>,
        "<a href="#forcetimezone" title="ForceTimezone">ForceTimezone</a>" : <i>Boolean</i>,
        "<a href="#hostname" title="HostName">HostName</a>" : <i>String</i>,
        "<a href="#manualprefixregexp" title="ManualPrefixRegexp">ManualPrefixRegexp</a>" : <i>String</i>,
        "<a href="#multilineprocessingenabled" title="MultilineProcessingEnabled">MultilineProcessingEnabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#paused" title="Paused">Paused</a>" : <i>Boolean</i>,
        "<a href="#scaninterval" title="ScanInterval">ScanInterval</a>" : <i>Double</i>,
        "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>,
        "<a href="#useautolinematching" title="UseAutolineMatching">UseAutolineMatching</a>" : <i>Boolean</i>,
        "<a href="#authentication" title="Authentication">Authentication</a>" : <i>[ <a href="authenticationdefinition.md">AuthenticationDefinition</a>, ... ]</i>,
        "<a href="#defaultdateformats" title="DefaultDateFormats">DefaultDateFormats</a>" : <i>[ <a href="defaultdateformatsdefinition.md">DefaultDateFormatsDefinition</a>, ... ]</i>,
        "<a href="#filters" title="Filters">Filters</a>" : <i>[ <a href="filtersdefinition.md">FiltersDefinition</a>, ... ]</i>,
        "<a href="#path" title="Path">Path</a>" : <i>[ <a href="pathdefinition.md">PathDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::SumoLogic::S3AuditSource
Properties:
    <a href="#automaticdateparsing" title="AutomaticDateParsing">AutomaticDateParsing</a>: <i>Boolean</i>
    <a href="#category" title="Category">Category</a>: <i>String</i>
    <a href="#collectorid" title="CollectorId">CollectorId</a>: <i>Double</i>
    <a href="#contenttype" title="ContentType">ContentType</a>: <i>String</i>
    <a href="#cutoffrelativetime" title="CutoffRelativeTime">CutoffRelativeTime</a>: <i>String</i>
    <a href="#cutofftimestamp" title="CutoffTimestamp">CutoffTimestamp</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#fields" title="Fields">Fields</a>: <i>
      - <a href="fieldsdefinition.md">FieldsDefinition</a></i>
    <a href="#forcetimezone" title="ForceTimezone">ForceTimezone</a>: <i>Boolean</i>
    <a href="#hostname" title="HostName">HostName</a>: <i>String</i>
    <a href="#manualprefixregexp" title="ManualPrefixRegexp">ManualPrefixRegexp</a>: <i>String</i>
    <a href="#multilineprocessingenabled" title="MultilineProcessingEnabled">MultilineProcessingEnabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#paused" title="Paused">Paused</a>: <i>Boolean</i>
    <a href="#scaninterval" title="ScanInterval">ScanInterval</a>: <i>Double</i>
    <a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
    <a href="#useautolinematching" title="UseAutolineMatching">UseAutolineMatching</a>: <i>Boolean</i>
    <a href="#authentication" title="Authentication">Authentication</a>: <i>
      - <a href="authenticationdefinition.md">AuthenticationDefinition</a></i>
    <a href="#defaultdateformats" title="DefaultDateFormats">DefaultDateFormats</a>: <i>
      - <a href="defaultdateformatsdefinition.md">DefaultDateFormatsDefinition</a></i>
    <a href="#filters" title="Filters">Filters</a>: <i>
      - <a href="filtersdefinition.md">FiltersDefinition</a></i>
    <a href="#path" title="Path">Path</a>: <i>
      - <a href="pathdefinition.md">PathDefinition</a></i>
</pre>

## Properties

#### AutomaticDateParsing

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Category

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CollectorId

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CutoffRelativeTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CutoffTimestamp

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fields

_Required_: No

_Type_: List of <a href="fieldsdefinition.md">FieldsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceTimezone

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManualPrefixRegexp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultilineProcessingEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Paused

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScanInterval

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseAutolineMatching

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authentication

_Required_: No

_Type_: List of <a href="authenticationdefinition.md">AuthenticationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultDateFormats

_Required_: No

_Type_: List of <a href="defaultdateformatsdefinition.md">DefaultDateFormatsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filters

_Required_: No

_Type_: List of <a href="filtersdefinition.md">FiltersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: No

_Type_: List of <a href="pathdefinition.md">PathDefinition</a>

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

#### Url

Returns the <code>Url</code> value.

