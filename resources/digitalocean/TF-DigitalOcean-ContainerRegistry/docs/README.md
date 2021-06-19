# TF::DigitalOcean::ContainerRegistry

Provides a DigitalOcean Container Registry resource. A Container Registry is
a secure, private location to store your containers for rapid deployment.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::DigitalOcean::ContainerRegistry",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#subscriptiontierslug" title="SubscriptionTierSlug">SubscriptionTierSlug</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::DigitalOcean::ContainerRegistry
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#subscriptiontierslug" title="SubscriptionTierSlug">SubscriptionTierSlug</a>: <i>String</i>
</pre>

## Properties

#### Name

The name of the container_registry.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubscriptionTierSlug

The slug identifier for the subscription tier to use (`starter`, `basic`, or `professional`).

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

#### Endpoint

Returns the <code>Endpoint</code> value.

#### Id

Returns the <code>Id</code> value.

#### ServerUrl

Returns the <code>ServerUrl</code> value.

