# Terraform::Gitlab::ProjectPushRules

CloudFormation equivalent of gitlab_project_push_rules

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Gitlab::ProjectPushRules",
    "Properties" : {
        "<a href="#authoremailregex" title="AuthorEmailRegex">AuthorEmailRegex</a>" : <i>String</i>,
        "<a href="#branchnameregex" title="BranchNameRegex">BranchNameRegex</a>" : <i>String</i>,
        "<a href="#commitmessageregex" title="CommitMessageRegex">CommitMessageRegex</a>" : <i>String</i>,
        "<a href="#denydeletetag" title="DenyDeleteTag">DenyDeleteTag</a>" : <i>Boolean</i>,
        "<a href="#filenameregex" title="FileNameRegex">FileNameRegex</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#maxfilesize" title="MaxFileSize">MaxFileSize</a>" : <i>Double</i>,
        "<a href="#membercheck" title="MemberCheck">MemberCheck</a>" : <i>Boolean</i>,
        "<a href="#preventsecrets" title="PreventSecrets">PreventSecrets</a>" : <i>Boolean</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Gitlab::ProjectPushRules
Properties:
    <a href="#authoremailregex" title="AuthorEmailRegex">AuthorEmailRegex</a>: <i>String</i>
    <a href="#branchnameregex" title="BranchNameRegex">BranchNameRegex</a>: <i>String</i>
    <a href="#commitmessageregex" title="CommitMessageRegex">CommitMessageRegex</a>: <i>String</i>
    <a href="#denydeletetag" title="DenyDeleteTag">DenyDeleteTag</a>: <i>Boolean</i>
    <a href="#filenameregex" title="FileNameRegex">FileNameRegex</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#maxfilesize" title="MaxFileSize">MaxFileSize</a>: <i>Double</i>
    <a href="#membercheck" title="MemberCheck">MemberCheck</a>: <i>Boolean</i>
    <a href="#preventsecrets" title="PreventSecrets">PreventSecrets</a>: <i>Boolean</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
</pre>

## Properties

#### AuthorEmailRegex

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BranchNameRegex

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommitMessageRegex

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DenyDeleteTag

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileNameRegex

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxFileSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemberCheck

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreventSecrets

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

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

