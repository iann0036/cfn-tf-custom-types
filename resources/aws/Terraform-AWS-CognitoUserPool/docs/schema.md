# Terraform::AWS::CognitoUserPool Schema

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#attributedatatype" title="AttributeDataType">AttributeDataType</a>" : <i>String</i>,
    "<a href="#developeronlyattribute" title="DeveloperOnlyAttribute">DeveloperOnlyAttribute</a>" : <i>Boolean</i>,
    "<a href="#mutable" title="Mutable">Mutable</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#required" title="Required">Required</a>" : <i>Boolean</i>,
    "<a href="#numberattributeconstraints" title="NumberAttributeConstraints">NumberAttributeConstraints</a>" : <i>[ &lt;a href=&#34;schema-numberattributeconstraints.md&#34;&gt;NumberAttributeConstraints&lt;/a&gt;, ... ]</i>,
    "<a href="#stringattributeconstraints" title="StringAttributeConstraints">StringAttributeConstraints</a>" : <i>[ &lt;a href=&#34;schema-stringattributeconstraints.md&#34;&gt;StringAttributeConstraints&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#attributedatatype" title="AttributeDataType">AttributeDataType</a>: <i>String</i>
<a href="#developeronlyattribute" title="DeveloperOnlyAttribute">DeveloperOnlyAttribute</a>: <i>Boolean</i>
<a href="#mutable" title="Mutable">Mutable</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#required" title="Required">Required</a>: <i>Boolean</i>
<a href="#numberattributeconstraints" title="NumberAttributeConstraints">NumberAttributeConstraints</a>: <i>
      - &lt;a href=&#34;schema-numberattributeconstraints.md&#34;&gt;NumberAttributeConstraints&lt;/a&gt;</i>
<a href="#stringattributeconstraints" title="StringAttributeConstraints">StringAttributeConstraints</a>: <i>
      - &lt;a href=&#34;schema-stringattributeconstraints.md&#34;&gt;StringAttributeConstraints&lt;/a&gt;</i>
</pre>

## Properties

#### AttributeDataType

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeveloperOnlyAttribute

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mutable

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Required

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberAttributeConstraints

_Required_: No
_Type_: List of &lt;a href=&#34;schema-numberattributeconstraints.md&#34;&gt;NumberAttributeConstraints&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StringAttributeConstraints

_Required_: No
_Type_: List of &lt;a href=&#34;schema-stringattributeconstraints.md&#34;&gt;StringAttributeConstraints&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

