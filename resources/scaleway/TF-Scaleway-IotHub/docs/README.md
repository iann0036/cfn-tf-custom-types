# TF::Scaleway::IotHub

-> **Note:** This terraform resource is currently in beta and might include breaking change in future releases.

Creates and manages Scaleway IoT Hub Instances. For more information, see [the documentation](https://developers.scaleway.com/en/products/iot/api).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Scaleway::IotHub",
    "Properties" : {
        "<a href="#deviceautoprovisioning" title="DeviceAutoProvisioning">DeviceAutoProvisioning</a>" : <i>Boolean</i>,
        "<a href="#disableevents" title="DisableEvents">DisableEvents</a>" : <i>Boolean</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#eventstopicprefix" title="EventsTopicPrefix">EventsTopicPrefix</a>" : <i>String</i>,
        "<a href="#hubca" title="HubCa">HubCa</a>" : <i>String</i>,
        "<a href="#hubcachallenge" title="HubCaChallenge">HubCaChallenge</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#productplan" title="ProductPlan">ProductPlan</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Scaleway::IotHub
Properties:
    <a href="#deviceautoprovisioning" title="DeviceAutoProvisioning">DeviceAutoProvisioning</a>: <i>Boolean</i>
    <a href="#disableevents" title="DisableEvents">DisableEvents</a>: <i>Boolean</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#eventstopicprefix" title="EventsTopicPrefix">EventsTopicPrefix</a>: <i>String</i>
    <a href="#hubca" title="HubCa">HubCa</a>: <i>String</i>
    <a href="#hubcachallenge" title="HubCaChallenge">HubCaChallenge</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#productplan" title="ProductPlan">ProductPlan</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
</pre>

## Properties

#### DeviceAutoProvisioning

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableEvents

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventsTopicPrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HubCa

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HubCaChallenge

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProductPlan

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

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

#### ConnectedDeviceCount

Returns the <code>ConnectedDeviceCount</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### DeviceCount

Returns the <code>DeviceCount</code> value.

#### Endpoint

Returns the <code>Endpoint</code> value.

#### Id

Returns the <code>Id</code> value.

#### OrganizationId

Returns the <code>OrganizationId</code> value.

#### Status

Returns the <code>Status</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.

