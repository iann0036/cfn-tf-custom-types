# TF::GitHub::Branch

This resource allows you to create and manage branches within your repository.

Additional constraints can be applied to ensure your branch is created from
another branch or commit.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GitHub::Branch",
    "Properties" : {
        "<a href="#branch" title="Branch">Branch</a>" : <i>String</i>,
        "<a href="#repository" title="Repository">Repository</a>" : <i>String</i>,
        "<a href="#sourcebranch" title="SourceBranch">SourceBranch</a>" : <i>String</i>,
        "<a href="#sourcesha" title="SourceSha">SourceSha</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GitHub::Branch
Properties:
    <a href="#branch" title="Branch">Branch</a>: <i>String</i>
    <a href="#repository" title="Repository">Repository</a>: <i>String</i>
    <a href="#sourcebranch" title="SourceBranch">SourceBranch</a>: <i>String</i>
    <a href="#sourcesha" title="SourceSha">SourceSha</a>: <i>String</i>
</pre>

## Properties

#### Branch

The repository branch to create.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repository

The GitHub repository name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceBranch

The branch name to start from. Defaults to `master`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceSha

The commit hash to start from. Defaults to the tip of `source_branch`. If provided, `source_branch` is ignored.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Etag

Returns the <code>Etag</code> value.

#### Id

Returns the <code>Id</code> value.

#### Ref

Returns the <code>Ref</code> value.

#### Sha

Returns the <code>Sha</code> value.

