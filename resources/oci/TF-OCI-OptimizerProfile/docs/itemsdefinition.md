# TF::OCI::OptimizerProfile ItemsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#tagdefinitionname" title="TagDefinitionName">TagDefinitionName</a>" : <i>String</i>,
    "<a href="#tagnamespacename" title="TagNamespaceName">TagNamespaceName</a>" : <i>String</i>,
    "<a href="#tagvaluetype" title="TagValueType">TagValueType</a>" : <i>String</i>,
    "<a href="#tagvalues" title="TagValues">TagValues</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#tagdefinitionname" title="TagDefinitionName">TagDefinitionName</a>: <i>String</i>
<a href="#tagnamespacename" title="TagNamespaceName">TagNamespaceName</a>: <i>String</i>
<a href="#tagvaluetype" title="TagValueType">TagValueType</a>: <i>String</i>
<a href="#tagvalues" title="TagValues">TagValues</a>: <i>
      - String</i>
</pre>

## Properties

#### TagDefinitionName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagNamespaceName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagValueType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagValues

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

