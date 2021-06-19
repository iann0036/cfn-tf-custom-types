# TF::Lacework::AlertChannelGcpPubSub

You can configure Lacework to forward events to Google Cloud Pub/Sub asynchronous messaging service using the Lacework Google Cloud Pub/Sub alert channel.

To find more information see the [Lacework support documentation](https://support.lacework.com/hc/en-us/articles/360047496514-Google-Cloud-Pub-Sub).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Lacework::AlertChannelGcpPubSub",
    "Properties" : {
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#issuegrouping" title="IssueGrouping">IssueGrouping</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#topicid" title="TopicId">TopicId</a>" : <i>String</i>,
        "<a href="#credentials" title="Credentials">Credentials</a>" : <i>[ <a href="credentialsdefinition.md">CredentialsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Lacework::AlertChannelGcpPubSub
Properties:
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#issuegrouping" title="IssueGrouping">IssueGrouping</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#topicid" title="TopicId">TopicId</a>: <i>String</i>
    <a href="#credentials" title="Credentials">Credentials</a>: <i>
      - <a href="credentialsdefinition.md">CredentialsDefinition</a></i>
</pre>

## Properties

#### Enabled

The state of the external integration. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IssueGrouping

Defines how Lacework compliance events get grouped. Must be one of `Events` or `Resources`. Defaults to `Events`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Alert Channel integration name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The name of the Google Cloud Project.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopicId

The ID of the Google Cloud Pub/Sub topic.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Credentials

_Required_: No

_Type_: List of <a href="credentialsdefinition.md">CredentialsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedOrUpdatedBy

Returns the <code>CreatedOrUpdatedBy</code> value.

#### CreatedOrUpdatedTime

Returns the <code>CreatedOrUpdatedTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### IntgGuid

Returns the <code>IntgGuid</code> value.

#### OrgLevel

Returns the <code>OrgLevel</code> value.

#### TypeName

Returns the <code>TypeName</code> value.

