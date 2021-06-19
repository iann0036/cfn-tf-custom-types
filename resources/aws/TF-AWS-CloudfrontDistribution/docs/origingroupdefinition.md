# TF::AWS::CloudfrontDistribution OriginGroupDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#originid" title="OriginId">OriginId</a>" : <i>String</i>,
    "<a href="#failovercriteria" title="FailoverCriteria">FailoverCriteria</a>" : <i>[ <a href="failovercriteriadefinition.md">FailoverCriteriaDefinition</a>, ... ]</i>,
    "<a href="#member" title="Member">Member</a>" : <i>[ <a href="memberdefinition.md">MemberDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#originid" title="OriginId">OriginId</a>: <i>String</i>
<a href="#failovercriteria" title="FailoverCriteria">FailoverCriteria</a>: <i>
      - <a href="failovercriteriadefinition.md">FailoverCriteriaDefinition</a></i>
<a href="#member" title="Member">Member</a>: <i>
      - <a href="memberdefinition.md">MemberDefinition</a></i>
</pre>

## Properties

#### OriginId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailoverCriteria

_Required_: No

_Type_: List of <a href="failovercriteriadefinition.md">FailoverCriteriaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Member

_Required_: No

_Type_: List of <a href="memberdefinition.md">MemberDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

