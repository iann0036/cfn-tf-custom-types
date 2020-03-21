# Terraform::Kubernetes::Pod Spec Volume Secret

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultmode" title="DefaultMode">DefaultMode</a>" : <i>String</i>,
    "<a href="#optional" title="Optional">Optional</a>" : <i>Boolean</i>,
    "<a href="#secretname" title="SecretName">SecretName</a>" : <i>String</i>,
    "<a href="#items" title="Items">Items</a>" : <i>[ <a href="spec-volume-secret-items.md">Items</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#defaultmode" title="DefaultMode">DefaultMode</a>: <i>String</i>
<a href="#optional" title="Optional">Optional</a>: <i>Boolean</i>
<a href="#secretname" title="SecretName">SecretName</a>: <i>String</i>
<a href="#items" title="Items">Items</a>: <i>
      - <a href="spec-volume-secret-items.md">Items</a></i>
</pre>

## Properties

#### DefaultMode

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Optional

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Items

_Required_: No
_Type_: List of <a href="spec-volume-secret-items.md">Items</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

