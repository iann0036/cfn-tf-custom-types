# TF::Thunder::SlbPlayerIdGlobal

`thunder_slb_player_id_global` Provides details about thunder SLB player id global

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbPlayerIdGlobal",
    "Properties" : {
        "<a href="#absmaxexpiration" title="AbsMaxExpiration">AbsMaxExpiration</a>" : <i>Double</i>,
        "<a href="#enable64bitplayerid" title="Enable64bitPlayerId">Enable64bitPlayerId</a>" : <i>Double</i>,
        "<a href="#enforcementtimer" title="EnforcementTimer">EnforcementTimer</a>" : <i>Double</i>,
        "<a href="#forcepassive" title="ForcePassive">ForcePassive</a>" : <i>Double</i>,
        "<a href="#minexpiration" title="MinExpiration">MinExpiration</a>" : <i>Double</i>,
        "<a href="#pktactivityexpiration" title="PktActivityExpiration">PktActivityExpiration</a>" : <i>Double</i>,
        "<a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>" : <i>[ <a href="samplingenabledefinition.md">SamplingEnableDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbPlayerIdGlobal
Properties:
    <a href="#absmaxexpiration" title="AbsMaxExpiration">AbsMaxExpiration</a>: <i>Double</i>
    <a href="#enable64bitplayerid" title="Enable64bitPlayerId">Enable64bitPlayerId</a>: <i>Double</i>
    <a href="#enforcementtimer" title="EnforcementTimer">EnforcementTimer</a>: <i>Double</i>
    <a href="#forcepassive" title="ForcePassive">ForcePassive</a>: <i>Double</i>
    <a href="#minexpiration" title="MinExpiration">MinExpiration</a>: <i>Double</i>
    <a href="#pktactivityexpiration" title="PktActivityExpiration">PktActivityExpiration</a>: <i>Double</i>
    <a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>: <i>
      - <a href="samplingenabledefinition.md">SamplingEnableDefinition</a></i>
</pre>

## Properties

#### AbsMaxExpiration

Absolute max record expiration value (default 10 minutes) (Absolute max record expiration time in minutes, default 10).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enable64bitPlayerId

Enable 64 bit player id check. Default is 32 bit.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnforcementTimer

Time to playerid enforcement after bootup (default 480 seconds) (Time to playerid enforcement in seconds, default 480).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForcePassive

Forces the device to be in passive mode (Only stats and no packet drops).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinExpiration

Minimum record expiration value (default 1 min) (Min record expiration time in minutes, default 1).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PktActivityExpiration

Packet activity record expiration value (default 5 minutes) (Packet activity record expiration time in minutes, default 5).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SamplingEnable

_Required_: No

_Type_: List of <a href="samplingenabledefinition.md">SamplingEnableDefinition</a>

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

