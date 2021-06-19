# TF::AzureRM::IotSecurityDeviceGroup AllowRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#connectiontoipnotallowed" title="ConnectionToIpNotAllowed">ConnectionToIpNotAllowed</a>" : <i>[ String, ... ]</i>,
    "<a href="#localusernotallowed" title="LocalUserNotAllowed">LocalUserNotAllowed</a>" : <i>[ String, ... ]</i>,
    "<a href="#processnotallowed" title="ProcessNotAllowed">ProcessNotAllowed</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#connectiontoipnotallowed" title="ConnectionToIpNotAllowed">ConnectionToIpNotAllowed</a>: <i>
      - String</i>
<a href="#localusernotallowed" title="LocalUserNotAllowed">LocalUserNotAllowed</a>: <i>
      - String</i>
<a href="#processnotallowed" title="ProcessNotAllowed">ProcessNotAllowed</a>: <i>
      - String</i>
</pre>

## Properties

#### ConnectionToIpNotAllowed

Specifies which Ip is not allowed to be connected to in current device group.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalUserNotAllowed

Specifies which local user is not allowed to Login in current device group.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessNotAllowed

Specifies which process is not allowed to be executed in current device group.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

