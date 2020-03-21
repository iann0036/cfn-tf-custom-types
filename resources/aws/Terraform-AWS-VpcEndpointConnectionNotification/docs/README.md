# Terraform::AWS::VpcEndpointConnectionNotification

CloudFormation equivalent of aws_vpc_endpoint_connection_notification

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::VpcEndpointConnectionNotification",
    "Properties" : {
        "<a href="#connectionevents" title="ConnectionEvents">ConnectionEvents</a>" : <i>[ String, ... ]</i>,
        "<a href="#connectionnotificationarn" title="ConnectionNotificationArn">ConnectionNotificationArn</a>" : <i>String</i>,
        "<a href="#vpcendpointid" title="VpcEndpointId">VpcEndpointId</a>" : <i>String</i>,
        "<a href="#vpcendpointserviceid" title="VpcEndpointServiceId">VpcEndpointServiceId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::VpcEndpointConnectionNotification
Properties:
    <a href="#connectionevents" title="ConnectionEvents">ConnectionEvents</a>: <i>
      - String</i>
    <a href="#connectionnotificationarn" title="ConnectionNotificationArn">ConnectionNotificationArn</a>: <i>String</i>
    <a href="#vpcendpointid" title="VpcEndpointId">VpcEndpointId</a>: <i>String</i>
    <a href="#vpcendpointserviceid" title="VpcEndpointServiceId">VpcEndpointServiceId</a>: <i>String</i>
</pre>

## Properties

#### ConnectionEvents

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionNotificationArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcEndpointId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcEndpointServiceId

_Required_: No

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

#### NotificationType

Returns the <code>NotificationType</code> value.

#### State

Returns the <code>State</code> value.

