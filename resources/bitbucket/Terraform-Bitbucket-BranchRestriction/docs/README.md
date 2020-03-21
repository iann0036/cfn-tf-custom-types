# Terraform::Bitbucket::BranchRestriction

Provides a Bitbucket branch restriction resource.

This allows you for setting up branch restrictions for your repository.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Bitbucket::BranchRestriction",
    "Properties" : {
        "<a href="#kind" title="Kind">Kind</a>" : <i>String</i>,
        "<a href="#owner" title="Owner">Owner</a>" : <i>String</i>,
        "<a href="#pattern" title="Pattern">Pattern</a>" : <i>String</i>,
        "<a href="#repository" title="Repository">Repository</a>" : <i>String</i>,
        "<a href="#users" title="Users">Users</a>" : <i>[ String, ... ]</i>,
        "<a href="#value" title="Value">Value</a>" : <i>Double</i>,
        "<a href="#groups" title="Groups">Groups</a>" : <i>[ <a href="groups.md">Groups</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Bitbucket::BranchRestriction
Properties:
    <a href="#kind" title="Kind">Kind</a>: <i>String</i>
    <a href="#owner" title="Owner">Owner</a>: <i>String</i>
    <a href="#pattern" title="Pattern">Pattern</a>: <i>String</i>
    <a href="#repository" title="Repository">Repository</a>: <i>String</i>
    <a href="#users" title="Users">Users</a>: <i>
      - String</i>
    <a href="#value" title="Value">Value</a>: <i>Double</i>
    <a href="#groups" title="Groups">Groups</a>: <i>
      - <a href="groups.md">Groups</a></i>
</pre>

## Properties

#### Kind

The type of restriction that is being applied. List of possible stages is [here](https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Busername%7D/%7Brepo_slug%7D/branch-restrictions).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owner

The owner of this repository. Can be you or any team you
have write access to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pattern

The pattern to determine which branches will be restricted.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repository

The name of the repository.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Users

A list of users to use.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Groups

_Required_: No

_Type_: List of <a href="groups.md">Groups</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

