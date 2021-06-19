# TF::PrismaCloud::Integration

Manages an integration.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::PrismaCloud::Integration",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#integrationtype" title="IntegrationType">IntegrationType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#integrationconfig" title="IntegrationConfig">IntegrationConfig</a>" : <i>[ <a href="integrationconfigdefinition.md">IntegrationConfigDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::PrismaCloud::Integration
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#integrationtype" title="IntegrationType">IntegrationType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#integrationconfig" title="IntegrationConfig">IntegrationConfig</a>: <i>
      - <a href="integrationconfigdefinition.md">IntegrationConfigDefinition</a></i>
</pre>

## Properties

#### Description

Description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationType

Integration type (valid values can be found [here](https://api.docs.prismacloud.io/reference#integrations).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the integration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationConfig

_Required_: No

_Type_: List of <a href="integrationconfigdefinition.md">IntegrationConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedBy

Returns the <code>CreatedBy</code> value.

#### CreatedTs

Returns the <code>CreatedTs</code> value.

#### Id

Returns the <code>Id</code> value.

#### IntegrationId

Returns the <code>IntegrationId</code> value.

#### LastModifiedBy

Returns the <code>LastModifiedBy</code> value.

#### LastModifiedTs

Returns the <code>LastModifiedTs</code> value.

#### Reason

Returns the <code>Reason</code> value.

#### Status

Returns the <code>Status</code> value.

#### Valid

Returns the <code>Valid</code> value.

