# TF::GoogleBeta::GoogleDataprocJob HiveConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#continueonfailure" title="ContinueOnFailure">ContinueOnFailure</a>" : <i>Boolean</i>,
    "<a href="#jarfileuris" title="JarFileUris">JarFileUris</a>" : <i>[ String, ... ]</i>,
    "<a href="#properties" title="Properties">Properties</a>" : <i>[ <a href="propertiesdefinition.md">PropertiesDefinition</a>, ... ]</i>,
    "<a href="#queryfileuri" title="QueryFileUri">QueryFileUri</a>" : <i>String</i>,
    "<a href="#querylist" title="QueryList">QueryList</a>" : <i>[ String, ... ]</i>,
    "<a href="#scriptvariables" title="ScriptVariables">ScriptVariables</a>" : <i>[ <a href="scriptvariablesdefinition.md">ScriptVariablesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#continueonfailure" title="ContinueOnFailure">ContinueOnFailure</a>: <i>Boolean</i>
<a href="#jarfileuris" title="JarFileUris">JarFileUris</a>: <i>
      - String</i>
<a href="#properties" title="Properties">Properties</a>: <i>
      - <a href="propertiesdefinition.md">PropertiesDefinition</a></i>
<a href="#queryfileuri" title="QueryFileUri">QueryFileUri</a>: <i>String</i>
<a href="#querylist" title="QueryList">QueryList</a>: <i>
      - String</i>
<a href="#scriptvariables" title="ScriptVariables">ScriptVariables</a>: <i>
      - <a href="scriptvariablesdefinition.md">ScriptVariablesDefinition</a></i>
</pre>

## Properties

#### ContinueOnFailure

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JarFileUris

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Properties

_Required_: No

_Type_: List of <a href="propertiesdefinition.md">PropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryFileUri

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryList

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScriptVariables

_Required_: No

_Type_: List of <a href="scriptvariablesdefinition.md">ScriptVariablesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

