# TF::AWS::SesConfigurationSet

Provides an SES configuration set resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::SesConfigurationSet",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#reputationmetricsenabled" title="ReputationMetricsEnabled">ReputationMetricsEnabled</a>" : <i>Boolean</i>,
        "<a href="#sendingenabled" title="SendingEnabled">SendingEnabled</a>" : <i>Boolean</i>,
        "<a href="#deliveryoptions" title="DeliveryOptions">DeliveryOptions</a>" : <i>[ <a href="deliveryoptionsdefinition.md">DeliveryOptionsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::SesConfigurationSet
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#reputationmetricsenabled" title="ReputationMetricsEnabled">ReputationMetricsEnabled</a>: <i>Boolean</i>
    <a href="#sendingenabled" title="SendingEnabled">SendingEnabled</a>: <i>Boolean</i>
    <a href="#deliveryoptions" title="DeliveryOptions">DeliveryOptions</a>: <i>
      - <a href="deliveryoptionsdefinition.md">DeliveryOptionsDefinition</a></i>
</pre>

## Properties

#### Name

Name of the configuration set.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReputationMetricsEnabled

Whether or not Amazon SES publishes reputation metrics for the configuration set, such as bounce and complaint rates, to Amazon CloudWatch. The default value is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendingEnabled

Whether email sending is enabled or disabled for the configuration set. The default value is `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeliveryOptions

_Required_: No

_Type_: List of <a href="deliveryoptionsdefinition.md">DeliveryOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastFreshStart

Returns the <code>LastFreshStart</code> value.

