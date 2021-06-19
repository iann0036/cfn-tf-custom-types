# TF::ACI::HsrpGroupPolicy

Manages ACI HSRP Group Policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::HsrpGroupPolicy",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#ctrl" title="Ctrl">Ctrl</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#hellointvl" title="HelloIntvl">HelloIntvl</a>" : <i>String</i>,
        "<a href="#holdintvl" title="HoldIntvl">HoldIntvl</a>" : <i>String</i>,
        "<a href="#hsrpgrouppolicytype" title="HsrpGroupPolicyType">HsrpGroupPolicyType</a>" : <i>String</i>,
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#preemptdelaymin" title="PreemptDelayMin">PreemptDelayMin</a>" : <i>String</i>,
        "<a href="#preemptdelayreload" title="PreemptDelayReload">PreemptDelayReload</a>" : <i>String</i>,
        "<a href="#preemptdelaysync" title="PreemptDelaySync">PreemptDelaySync</a>" : <i>String</i>,
        "<a href="#prio" title="Prio">Prio</a>" : <i>String</i>,
        "<a href="#tenantdn" title="TenantDn">TenantDn</a>" : <i>String</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::HsrpGroupPolicy
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#ctrl" title="Ctrl">Ctrl</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#hellointvl" title="HelloIntvl">HelloIntvl</a>: <i>String</i>
    <a href="#holdintvl" title="HoldIntvl">HoldIntvl</a>: <i>String</i>
    <a href="#hsrpgrouppolicytype" title="HsrpGroupPolicyType">HsrpGroupPolicyType</a>: <i>String</i>
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#preemptdelaymin" title="PreemptDelayMin">PreemptDelayMin</a>: <i>String</i>
    <a href="#preemptdelayreload" title="PreemptDelayReload">PreemptDelayReload</a>: <i>String</i>
    <a href="#preemptdelaysync" title="PreemptDelaySync">PreemptDelaySync</a>: <i>String</i>
    <a href="#prio" title="Prio">Prio</a>: <i>String</i>
    <a href="#tenantdn" title="TenantDn">TenantDn</a>: <i>String</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>String</i>
</pre>

## Properties

#### Annotation

Annotation for object hsrp group policy.
- `description` - (Optional) Description for object hsrp group policy.
- `ctrl` - (Optional) The control state.
Allowed values: "preempt", "0". Default value: "0".
- `hello_intvl` - (Optional) The hello interval. Default value: "3000".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ctrl

The control state.
Allowed values: "preempt", "0". Default value: "0".
- `hello_intvl` - (Optional) The hello interval. Default value: "3000".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description for object hsrp group policy.
- `ctrl` - (Optional) The control state.
Allowed values: "preempt", "0". Default value: "0".
- `hello_intvl` - (Optional) The hello interval. Default value: "3000".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HelloIntvl

The hello interval. Default value: "3000".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HoldIntvl

The period of time before declaring that the neighbor is down. Default value: "10000".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsrpGroupPolicyType

The specific type of the object or component.
Allowed values: "md5", "simple". Default value: "simple".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

The key or password used to uniquely identify this configuration object. If `key` is set, the object key will reset when terraform configuration is applied. Default value: "cisco".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of Object hsrp group policy.
- `annotation` - (Optional) Annotation for object hsrp group policy.
- `description` - (Optional) Description for object hsrp group policy.
- `ctrl` - (Optional) The control state.
Allowed values: "preempt", "0". Default value: "0".
- `hello_intvl` - (Optional) The hello interval. Default value: "3000".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

Name alias for object hsrp group policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreemptDelayMin

HSRP Group's Minimum Preemption delay. Default value: "0".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreemptDelayReload

Preemption delay after switch reboot. Default value: "0".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreemptDelaySync

Maximum number of seconds to allow IPredundancy clients to prevent preemption. Default value: "0".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prio

The QoS priority class ID. Default value: "100".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantDn

Distinguished name of parent tenant object.
- `name` - (Required) Name of Object hsrp group policy.
- `annotation` - (Optional) Annotation for object hsrp group policy.
- `description` - (Optional) Description for object hsrp group policy.
- `ctrl` - (Optional) The control state.
Allowed values: "preempt", "0". Default value: "0".
- `hello_intvl` - (Optional) The hello interval. Default value: "3000".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

Amount of time between authentication attempts. Default value: "0".

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

#### Id

Returns the <code>Id</code> value.

