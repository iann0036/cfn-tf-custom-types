# Terraform::Gitlab::ProjectPushRules

This resource allows you to create and manage push rules for your GitLab projects.
For further information on push rules, consult the [gitlab
documentation](https://docs.gitlab.com/ce/push_rules/push_rules.html#push-rules).

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
    <a href="#maxfilesize" title="MaxFileSize">MaxFileSize</a>: <i>Double</i>
    <a href="#membercheck" title="MemberCheck">MemberCheck</a>: <i>Boolean</i>
    <a href="#preventsecrets" title="PreventSecrets">PreventSecrets</a>: <i>Boolean</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
</pre>

## Properties

#### AuthorEmailRegex

All commit author emails must match this regex, e.g. "@my-company.com$".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BranchNameRegex

All branch names must match this regex, e.g. "(feature|hotfix)\/*".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommitMessageRegex

All commit messages must match this regex, e.g. "Fixed \d+\..*".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DenyDeleteTag

Deny deleting a tag.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileNameRegex

All commited filenames must not match this regex, e.g. "(jar|exe)$".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxFileSize

Maximum file size (MB).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemberCheck

Restrict commits by author (email) to existing GitLab users.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreventSecrets

GitLab will reject any files that are likely to contain secrets.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The name or id of the project to add the push rules to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

