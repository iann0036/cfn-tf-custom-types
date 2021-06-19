# TF::FortiOS::Switchcontroller8021Xsettings

Configure global 802.1X settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::Switchcontroller8021Xsettings",
    "Properties" : {
        "<a href="#linkdownauth" title="LinkDownAuth">LinkDownAuth</a>" : <i>String</i>,
        "<a href="#maxreauthattempt" title="MaxReauthAttempt">MaxReauthAttempt</a>" : <i>Double</i>,
        "<a href="#reauthperiod" title="ReauthPeriod">ReauthPeriod</a>" : <i>Double</i>,
        "<a href="#txperiod" title="TxPeriod">TxPeriod</a>" : <i>Double</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::Switchcontroller8021Xsettings
Properties:
    <a href="#linkdownauth" title="LinkDownAuth">LinkDownAuth</a>: <i>String</i>
    <a href="#maxreauthattempt" title="MaxReauthAttempt">MaxReauthAttempt</a>: <i>Double</i>
    <a href="#reauthperiod" title="ReauthPeriod">ReauthPeriod</a>: <i>Double</i>
    <a href="#txperiod" title="TxPeriod">TxPeriod</a>: <i>Double</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### LinkDownAuth

Interface-reauthentication state to set if a link is down. Valid values: `set-unauth`, `no-action`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxReauthAttempt

Maximum number of authentication attempts (0 - 15, default = 3).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReauthPeriod

Period of time to allow for reauthentication (1 - 1440 sec, default = 60, 0 = disable reauthentication).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TxPeriod

802.1X Tx period (seconds, default=30).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

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

