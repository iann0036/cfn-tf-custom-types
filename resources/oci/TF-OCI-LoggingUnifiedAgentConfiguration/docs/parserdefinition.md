# TF::OCI::LoggingUnifiedAgentConfiguration ParserDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#delimiter" title="Delimiter">Delimiter</a>" : <i>String</i>,
    "<a href="#expression" title="Expression">Expression</a>" : <i>String</i>,
    "<a href="#fieldtimekey" title="FieldTimeKey">FieldTimeKey</a>" : <i>String</i>,
    "<a href="#format" title="Format">Format</a>" : <i>[ String, ... ]</i>,
    "<a href="#formatfirstline" title="FormatFirstline">FormatFirstline</a>" : <i>String</i>,
    "<a href="#grokfailurekey" title="GrokFailureKey">GrokFailureKey</a>" : <i>String</i>,
    "<a href="#groknamekey" title="GrokNameKey">GrokNameKey</a>" : <i>String</i>,
    "<a href="#isestimatecurrentevent" title="IsEstimateCurrentEvent">IsEstimateCurrentEvent</a>" : <i>Boolean</i>,
    "<a href="#iskeeptimekey" title="IsKeepTimeKey">IsKeepTimeKey</a>" : <i>Boolean</i>,
    "<a href="#isnullemptystring" title="IsNullEmptyString">IsNullEmptyString</a>" : <i>Boolean</i>,
    "<a href="#issupportcolonlessident" title="IsSupportColonlessIdent">IsSupportColonlessIdent</a>" : <i>Boolean</i>,
    "<a href="#iswithpriority" title="IsWithPriority">IsWithPriority</a>" : <i>Boolean</i>,
    "<a href="#keys" title="Keys">Keys</a>" : <i>[ String, ... ]</i>,
    "<a href="#messageformat" title="MessageFormat">MessageFormat</a>" : <i>String</i>,
    "<a href="#messagekey" title="MessageKey">MessageKey</a>" : <i>String</i>,
    "<a href="#multilinestartregexp" title="MultiLineStartRegexp">MultiLineStartRegexp</a>" : <i>String</i>,
    "<a href="#nullvaluepattern" title="NullValuePattern">NullValuePattern</a>" : <i>String</i>,
    "<a href="#parsertype" title="ParserType">ParserType</a>" : <i>String</i>,
    "<a href="#rfc5424timeformat" title="Rfc5424timeFormat">Rfc5424timeFormat</a>" : <i>String</i>,
    "<a href="#syslogparsertype" title="SyslogParserType">SyslogParserType</a>" : <i>String</i>,
    "<a href="#timeformat" title="TimeFormat">TimeFormat</a>" : <i>String</i>,
    "<a href="#timetype" title="TimeType">TimeType</a>" : <i>String</i>,
    "<a href="#timeoutinmilliseconds" title="TimeoutInMilliseconds">TimeoutInMilliseconds</a>" : <i>Double</i>,
    "<a href="#types" title="Types">Types</a>" : <i>[ <a href="typesdefinition.md">TypesDefinition</a>, ... ]</i>,
    "<a href="#patterns" title="Patterns">Patterns</a>" : <i>[ <a href="patternsdefinition.md">PatternsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#delimiter" title="Delimiter">Delimiter</a>: <i>String</i>
<a href="#expression" title="Expression">Expression</a>: <i>String</i>
<a href="#fieldtimekey" title="FieldTimeKey">FieldTimeKey</a>: <i>String</i>
<a href="#format" title="Format">Format</a>: <i>
      - String</i>
<a href="#formatfirstline" title="FormatFirstline">FormatFirstline</a>: <i>String</i>
<a href="#grokfailurekey" title="GrokFailureKey">GrokFailureKey</a>: <i>String</i>
<a href="#groknamekey" title="GrokNameKey">GrokNameKey</a>: <i>String</i>
<a href="#isestimatecurrentevent" title="IsEstimateCurrentEvent">IsEstimateCurrentEvent</a>: <i>Boolean</i>
<a href="#iskeeptimekey" title="IsKeepTimeKey">IsKeepTimeKey</a>: <i>Boolean</i>
<a href="#isnullemptystring" title="IsNullEmptyString">IsNullEmptyString</a>: <i>Boolean</i>
<a href="#issupportcolonlessident" title="IsSupportColonlessIdent">IsSupportColonlessIdent</a>: <i>Boolean</i>
<a href="#iswithpriority" title="IsWithPriority">IsWithPriority</a>: <i>Boolean</i>
<a href="#keys" title="Keys">Keys</a>: <i>
      - String</i>
<a href="#messageformat" title="MessageFormat">MessageFormat</a>: <i>String</i>
<a href="#messagekey" title="MessageKey">MessageKey</a>: <i>String</i>
<a href="#multilinestartregexp" title="MultiLineStartRegexp">MultiLineStartRegexp</a>: <i>String</i>
<a href="#nullvaluepattern" title="NullValuePattern">NullValuePattern</a>: <i>String</i>
<a href="#parsertype" title="ParserType">ParserType</a>: <i>String</i>
<a href="#rfc5424timeformat" title="Rfc5424timeFormat">Rfc5424timeFormat</a>: <i>String</i>
<a href="#syslogparsertype" title="SyslogParserType">SyslogParserType</a>: <i>String</i>
<a href="#timeformat" title="TimeFormat">TimeFormat</a>: <i>String</i>
<a href="#timetype" title="TimeType">TimeType</a>: <i>String</i>
<a href="#timeoutinmilliseconds" title="TimeoutInMilliseconds">TimeoutInMilliseconds</a>: <i>Double</i>
<a href="#types" title="Types">Types</a>: <i>
      - <a href="typesdefinition.md">TypesDefinition</a></i>
<a href="#patterns" title="Patterns">Patterns</a>: <i>
      - <a href="patternsdefinition.md">PatternsDefinition</a></i>
</pre>

## Properties

#### Delimiter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expression

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FieldTimeKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Format

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FormatFirstline

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GrokFailureKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GrokNameKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsEstimateCurrentEvent

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsKeepTimeKey

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsNullEmptyString

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsSupportColonlessIdent

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsWithPriority

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Keys

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultiLineStartRegexp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NullValuePattern

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParserType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rfc5424timeFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyslogParserType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutInMilliseconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Types

_Required_: No

_Type_: List of <a href="typesdefinition.md">TypesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Patterns

_Required_: No

_Type_: List of <a href="patternsdefinition.md">PatternsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

