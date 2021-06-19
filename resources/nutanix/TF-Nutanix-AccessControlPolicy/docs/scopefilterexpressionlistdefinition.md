# TF::Nutanix::AccessControlPolicy ScopeFilterExpressionListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#lefthandside" title="LeftHandSide">LeftHandSide</a>" : <i>String</i>,
    "<a href="#operator" title="Operator">Operator</a>" : <i>String</i>,
    "<a href="#righthandside" title="RightHandSide">RightHandSide</a>" : <i>[ <a href="righthandsidedefinition.md">RightHandSideDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#lefthandside" title="LeftHandSide">LeftHandSide</a>: <i>String</i>
<a href="#operator" title="Operator">Operator</a>: <i>String</i>
<a href="#righthandside" title="RightHandSide">RightHandSide</a>: <i>
      - <a href="righthandsidedefinition.md">RightHandSideDefinition</a></i>
</pre>

## Properties

#### LeftHandSide

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Operator

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RightHandSide

_Required_: No

_Type_: List of <a href="righthandsidedefinition.md">RightHandSideDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

