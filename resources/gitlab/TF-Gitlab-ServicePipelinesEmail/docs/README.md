# TF::Gitlab::ServicePipelinesEmail

This resource manages a [Pipelines email integration](https://docs.gitlab.com/ee/user/project/integrations/overview.html#integrations-listing) that emails the pipeline status to a list of recipients.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Gitlab::ServicePipelinesEmail",
    "Properties" : {
        "<a href="#branchestobenotified" title="BranchesToBeNotified">BranchesToBeNotified</a>" : <i>String</i>,
        "<a href="#notifyonlybrokenpipelines" title="NotifyOnlyBrokenPipelines">NotifyOnlyBrokenPipelines</a>" : <i>Boolean</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#recipients" title="Recipients">Recipients</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Gitlab::ServicePipelinesEmail
Properties:
    <a href="#branchestobenotified" title="BranchesToBeNotified">BranchesToBeNotified</a>: <i>String</i>
    <a href="#notifyonlybrokenpipelines" title="NotifyOnlyBrokenPipelines">NotifyOnlyBrokenPipelines</a>: <i>Boolean</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#recipients" title="Recipients">Recipients</a>: <i>
      - String</i>
</pre>

## Properties

#### BranchesToBeNotified

Branches to send notifications for. Valid options are `all`, `default`, `protected`, and `default_and_protected`. Default is `default`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyOnlyBrokenPipelines

Notify only broken pipelines. Default is true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

ID of the project you want to activate integration on.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recipients

) email addresses where notifications are sent.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

