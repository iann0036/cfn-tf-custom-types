# TF::GitHub::RepositoryPullRequest

CloudFormation equivalent of github_repository_pull_request

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GitHub::RepositoryPullRequest",
    "Properties" : {
        "<a href="#baseref" title="BaseRef">BaseRef</a>" : <i>String</i>,
        "<a href="#baserepository" title="BaseRepository">BaseRepository</a>" : <i>String</i>,
        "<a href="#body" title="Body">Body</a>" : <i>String</i>,
        "<a href="#headref" title="HeadRef">HeadRef</a>" : <i>String</i>,
        "<a href="#maintainercanmodify" title="MaintainerCanModify">MaintainerCanModify</a>" : <i>Boolean</i>,
        "<a href="#owner" title="Owner">Owner</a>" : <i>String</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::GitHub::RepositoryPullRequest
Properties:
    <a href="#baseref" title="BaseRef">BaseRef</a>: <i>String</i>
    <a href="#baserepository" title="BaseRepository">BaseRepository</a>: <i>String</i>
    <a href="#body" title="Body">Body</a>: <i>String</i>
    <a href="#headref" title="HeadRef">HeadRef</a>: <i>String</i>
    <a href="#maintainercanmodify" title="MaintainerCanModify">MaintainerCanModify</a>: <i>Boolean</i>
    <a href="#owner" title="Owner">Owner</a>: <i>String</i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
</pre>

## Properties

#### BaseRef

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BaseRepository

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Body

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeadRef

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintainerCanModify

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owner

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

_Required_: Yes

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

#### BaseSha

Returns the <code>BaseSha</code> value.

#### Draft

Returns the <code>Draft</code> value.

#### HeadSha

Returns the <code>HeadSha</code> value.

#### Id

Returns the <code>Id</code> value.

#### Labels

Returns the <code>Labels</code> value.

#### Number

Returns the <code>Number</code> value.

#### OpenedAt

Returns the <code>OpenedAt</code> value.

#### OpenedBy

Returns the <code>OpenedBy</code> value.

#### State

Returns the <code>State</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.

