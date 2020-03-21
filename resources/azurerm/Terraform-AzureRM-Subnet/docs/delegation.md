# Terraform::AzureRM::Subnet Delegation

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#servicedelegation" title="ServiceDelegation">ServiceDelegation</a>" : <i>[ <a href="delegation-servicedelegation.md">ServiceDelegation</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#servicedelegation" title="ServiceDelegation">ServiceDelegation</a>: <i>
      - <a href="delegation-servicedelegation.md">ServiceDelegation</a></i>
</pre>

## Properties

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceDelegation

_Required_: No

_Type_: List of <a href="delegation-servicedelegation.md">ServiceDelegation</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

