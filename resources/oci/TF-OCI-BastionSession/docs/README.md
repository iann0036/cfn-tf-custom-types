# TF::OCI::BastionSession

This resource provides the Session resource in Oracle Cloud Infrastructure Bastion service.

Creates a new session in a bastion. A bastion session lets authorized users connect to a target resource for a predetermined amount of time. The Bastion service recognizes two types of sessions, managed SSH sessions and SSH port forwarding sessions. Managed SSH sessions require that the target resource has an OpenSSH server and the Oracle Cloud Agent both running.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::BastionSession",
    "Properties" : {
        "<a href="#bastionid" title="BastionId">BastionId</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#keytype" title="KeyType">KeyType</a>" : <i>String</i>,
        "<a href="#sessionttlinseconds" title="SessionTtlInSeconds">SessionTtlInSeconds</a>" : <i>Double</i>,
        "<a href="#keydetails" title="KeyDetails">KeyDetails</a>" : <i>[ <a href="keydetailsdefinition.md">KeyDetailsDefinition</a>, ... ]</i>,
        "<a href="#targetresourcedetails" title="TargetResourceDetails">TargetResourceDetails</a>" : <i>[ <a href="targetresourcedetailsdefinition.md">TargetResourceDetailsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::BastionSession
Properties:
    <a href="#bastionid" title="BastionId">BastionId</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#keytype" title="KeyType">KeyType</a>: <i>String</i>
    <a href="#sessionttlinseconds" title="SessionTtlInSeconds">SessionTtlInSeconds</a>: <i>Double</i>
    <a href="#keydetails" title="KeyDetails">KeyDetails</a>: <i>
      - <a href="keydetailsdefinition.md">KeyDetailsDefinition</a></i>
    <a href="#targetresourcedetails" title="TargetResourceDetails">TargetResourceDetails</a>: <i>
      - <a href="targetresourcedetailsdefinition.md">TargetResourceDetailsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### BastionId

The unique identifier (OCID) of the bastion on which to create this session.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) The name of the session.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyType

The type of the key used to connect to the session. PUB is a standard public key in OpenSSH format.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionTtlInSeconds

The amount of time the session can remain active.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyDetails

_Required_: No

_Type_: List of <a href="keydetailsdefinition.md">KeyDetailsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetResourceDetails

_Required_: No

_Type_: List of <a href="targetresourcedetailsdefinition.md">TargetResourceDetailsDefinition</a>

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

#### BastionName

Returns the <code>BastionName</code> value.

#### BastionPublicHostKeyInfo

Returns the <code>BastionPublicHostKeyInfo</code> value.

#### BastionUserName

Returns the <code>BastionUserName</code> value.

#### Id

Returns the <code>Id</code> value.

#### LifecycleDetails

Returns the <code>LifecycleDetails</code> value.

#### SshMetadata

Returns the <code>SshMetadata</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### TimeUpdated

Returns the <code>TimeUpdated</code> value.

