# TF::Gitlab::Project PushRulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authoremailregex" title="AuthorEmailRegex">AuthorEmailRegex</a>" : <i>String</i>,
    "<a href="#branchnameregex" title="BranchNameRegex">BranchNameRegex</a>" : <i>String</i>,
    "<a href="#commitcommittercheck" title="CommitCommitterCheck">CommitCommitterCheck</a>" : <i>Boolean</i>,
    "<a href="#commitmessagenegativeregex" title="CommitMessageNegativeRegex">CommitMessageNegativeRegex</a>" : <i>String</i>,
    "<a href="#commitmessageregex" title="CommitMessageRegex">CommitMessageRegex</a>" : <i>String</i>,
    "<a href="#denydeletetag" title="DenyDeleteTag">DenyDeleteTag</a>" : <i>Boolean</i>,
    "<a href="#filenameregex" title="FileNameRegex">FileNameRegex</a>" : <i>String</i>,
    "<a href="#maxfilesize" title="MaxFileSize">MaxFileSize</a>" : <i>Double</i>,
    "<a href="#membercheck" title="MemberCheck">MemberCheck</a>" : <i>Boolean</i>,
    "<a href="#preventsecrets" title="PreventSecrets">PreventSecrets</a>" : <i>Boolean</i>,
    "<a href="#rejectunsignedcommits" title="RejectUnsignedCommits">RejectUnsignedCommits</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#authoremailregex" title="AuthorEmailRegex">AuthorEmailRegex</a>: <i>String</i>
<a href="#branchnameregex" title="BranchNameRegex">BranchNameRegex</a>: <i>String</i>
<a href="#commitcommittercheck" title="CommitCommitterCheck">CommitCommitterCheck</a>: <i>Boolean</i>
<a href="#commitmessagenegativeregex" title="CommitMessageNegativeRegex">CommitMessageNegativeRegex</a>: <i>String</i>
<a href="#commitmessageregex" title="CommitMessageRegex">CommitMessageRegex</a>: <i>String</i>
<a href="#denydeletetag" title="DenyDeleteTag">DenyDeleteTag</a>: <i>Boolean</i>
<a href="#filenameregex" title="FileNameRegex">FileNameRegex</a>: <i>String</i>
<a href="#maxfilesize" title="MaxFileSize">MaxFileSize</a>: <i>Double</i>
<a href="#membercheck" title="MemberCheck">MemberCheck</a>: <i>Boolean</i>
<a href="#preventsecrets" title="PreventSecrets">PreventSecrets</a>: <i>Boolean</i>
<a href="#rejectunsignedcommits" title="RejectUnsignedCommits">RejectUnsignedCommits</a>: <i>Boolean</i>
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

#### CommitCommitterCheck

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommitMessageNegativeRegex

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

#### RejectUnsignedCommits

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

