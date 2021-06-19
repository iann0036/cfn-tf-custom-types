# TF::Scaleway::IotNetwork

-> **Note:** This terraform resource is currently in beta and might include breaking change in future releases.

Creates and manages Scaleway IoT Networks. For more information, see the following:

- [API documentation](https://developers.scaleway.com/en/products/iot/api).
- [Product documentation](https://www.scaleway.com/en/docs/scaleway-iothub-networks/)

For more step-by-step instructions on how to setup the networks on the external providers backends, you can follow these guides:

- [Configuring the Sigfox backend](https://www.scaleway.com/en/docs/scaleway-iothub-networks/#-Configuring-the-Sigfox-backend)
- [Using the Rest Network](https://www.scaleway.com/en/docs/scaleway-iothub-networks/#-Using-the-Rest-Network)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Scaleway::IotNetwork",
    "Properties" : {
        "<a href="#hubid" title="HubId">HubId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#topicprefix" title="TopicPrefix">TopicPrefix</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Scaleway::IotNetwork
Properties:
    <a href="#hubid" title="HubId">HubId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#topicprefix" title="TopicPrefix">TopicPrefix</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### HubId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopicPrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

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

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### Endpoint

Returns the <code>Endpoint</code> value.

#### Id

Returns the <code>Id</code> value.

#### Secret

Returns the <code>Secret</code> value.

