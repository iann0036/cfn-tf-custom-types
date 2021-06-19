# TF::Gridscale::Paas

Provides a PaaS resource. This can be used to create, modify, and delete PaaS instances.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Gridscale::Paas",
    "Properties" : {
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#securityzoneuuid" title="SecurityZoneUuid">SecurityZoneUuid</a>" : <i>String</i>,
        "<a href="#servicetemplateuuid" title="ServiceTemplateUuid">ServiceTemplateUuid</a>" : <i>String</i>,
        "<a href="#parameter" title="Parameter">Parameter</a>" : <i>[ <a href="parameterdefinition.md">ParameterDefinition</a>, ... ]</i>,
        "<a href="#resourcelimit" title="ResourceLimit">ResourceLimit</a>" : <i>[ <a href="resourcelimitdefinition.md">ResourceLimitDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Gridscale::Paas
Properties:
    <a href="#labels" title="Labels">Labels</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#securityzoneuuid" title="SecurityZoneUuid">SecurityZoneUuid</a>: <i>String</i>
    <a href="#servicetemplateuuid" title="ServiceTemplateUuid">ServiceTemplateUuid</a>: <i>String</i>
    <a href="#parameter" title="Parameter">Parameter</a>: <i>
      - <a href="parameterdefinition.md">ParameterDefinition</a></i>
    <a href="#resourcelimit" title="ResourceLimit">ResourceLimit</a>: <i>
      - <a href="resourcelimitdefinition.md">ResourceLimitDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Labels

List of labels in the format [ "label1", "label2" ].

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The human-readable name of the object. It supports the full UTF-8 character set, with a maximum of 64 characters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityZoneUuid

The UUID of the security zone that the service is running in.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceTemplateUuid

The template used to create the service.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameter

_Required_: No

_Type_: List of <a href="parameterdefinition.md">ParameterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceLimit

_Required_: No

_Type_: List of <a href="resourcelimitdefinition.md">ResourceLimitDefinition</a>

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

#### ChangeTime

Returns the <code>ChangeTime</code> value.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### CurrentPrice

Returns the <code>CurrentPrice</code> value.

#### Id

Returns the <code>Id</code> value.

#### Kubeconfig

Returns the <code>Kubeconfig</code> value.

#### ListenPort

Returns the <code>ListenPort</code> value.

#### NetworkUuid

Returns the <code>NetworkUuid</code> value.

#### Password

Returns the <code>Password</code> value.

#### ServiceTemplateUuidComputed

Returns the <code>ServiceTemplateUuidComputed</code> value.

#### Status

Returns the <code>Status</code> value.

#### UsageInMinute

Returns the <code>UsageInMinute</code> value.

#### Username

Returns the <code>Username</code> value.

