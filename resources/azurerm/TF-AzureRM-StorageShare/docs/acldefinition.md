# TF::AzureRM::StorageShare AclDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#accesspolicy" title="AccessPolicy">AccessPolicy</a>" : <i>[ <a href="accesspolicydefinition.md">AccessPolicyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#accesspolicy" title="AccessPolicy">AccessPolicy</a>: <i>
      - <a href="accesspolicydefinition.md">AccessPolicyDefinition</a></i>
</pre>

## Properties

#### Id

The ID which should be used for this Shared Identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessPolicy

_Required_: No

_Type_: List of <a href="accesspolicydefinition.md">AccessPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
