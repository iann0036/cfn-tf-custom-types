# TF::Google::DataprocWorkflowTemplate PrestoJobDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clienttags" title="ClientTags">ClientTags</a>" : <i>[ String, ... ]</i>,
    "<a href="#continueonfailure" title="ContinueOnFailure">ContinueOnFailure</a>" : <i>Boolean</i>,
    "<a href="#outputformat" title="OutputFormat">OutputFormat</a>" : <i>String</i>,
    "<a href="#properties" title="Properties">Properties</a>" : <i>[ <a href="propertiesdefinition.md">PropertiesDefinition</a>, ... ]</i>,
    "<a href="#queryfileuri" title="QueryFileUri">QueryFileUri</a>" : <i>String</i>,
    "<a href="#loggingconfig" title="LoggingConfig">LoggingConfig</a>" : <i>[ <a href="loggingconfigdefinition.md">LoggingConfigDefinition</a>, ... ]</i>,
    "<a href="#querylist" title="QueryList">QueryList</a>" : <i>[ <a href="querylistdefinition.md">QueryListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#clienttags" title="ClientTags">ClientTags</a>: <i>
      - String</i>
<a href="#continueonfailure" title="ContinueOnFailure">ContinueOnFailure</a>: <i>Boolean</i>
<a href="#outputformat" title="OutputFormat">OutputFormat</a>: <i>String</i>
<a href="#properties" title="Properties">Properties</a>: <i>
      - <a href="propertiesdefinition.md">PropertiesDefinition</a></i>
<a href="#queryfileuri" title="QueryFileUri">QueryFileUri</a>: <i>String</i>
<a href="#loggingconfig" title="LoggingConfig">LoggingConfig</a>: <i>
      - <a href="loggingconfigdefinition.md">LoggingConfigDefinition</a></i>
<a href="#querylist" title="QueryList">QueryList</a>: <i>
      - <a href="querylistdefinition.md">QueryListDefinition</a></i>
</pre>

## Properties

#### ClientTags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContinueOnFailure

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Properties

_Required_: No

_Type_: List of <a href="propertiesdefinition.md">PropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryFileUri

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingConfig

_Required_: No

_Type_: List of <a href="loggingconfigdefinition.md">LoggingConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryList

_Required_: No

_Type_: List of <a href="querylistdefinition.md">QueryListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

