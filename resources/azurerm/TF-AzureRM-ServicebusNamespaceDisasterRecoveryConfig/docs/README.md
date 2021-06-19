# TF::AzureRM::ServicebusNamespaceDisasterRecoveryConfig

Manages a Disaster Recovery Config for a Service Bus Namespace.

~> **NOTE:** Disaster Recovery Config is a Premium Sku only capability.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::ServicebusNamespaceDisasterRecoveryConfig",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#partnernamespaceid" title="PartnerNamespaceId">PartnerNamespaceId</a>" : <i>String</i>,
        "<a href="#primarynamespaceid" title="PrimaryNamespaceId">PrimaryNamespaceId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::ServicebusNamespaceDisasterRecoveryConfig
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#partnernamespaceid" title="PartnerNamespaceId">PartnerNamespaceId</a>: <i>String</i>
    <a href="#primarynamespaceid" title="PrimaryNamespaceId">PrimaryNamespaceId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Name

Specifies the name of the Disaster Recovery Config. This is the alias DNS name that will be created. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PartnerNamespaceId

The ID of the Service Bus Namespace to replicate to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryNamespaceId

The ID of the primary Service Bus Namespace to replicate. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AliasPrimaryConnectionString

Returns the <code>AliasPrimaryConnectionString</code> value.

#### AliasSecondaryConnectionString

Returns the <code>AliasSecondaryConnectionString</code> value.

#### DefaultPrimaryKey

Returns the <code>DefaultPrimaryKey</code> value.

#### DefaultSecondaryKey

Returns the <code>DefaultSecondaryKey</code> value.

#### Id

Returns the <code>Id</code> value.

