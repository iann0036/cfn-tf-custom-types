# TF::NewRelic::ApplicationSettings

-> **NOTE:** Applications are not created by this resource, but are created by
a reporting agent.

Use this resource to manage configuration for an application that already
exists in New Relic.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NewRelic::ApplicationSettings",
    "Properties" : {
        "<a href="#appapdexthreshold" title="AppApdexThreshold">AppApdexThreshold</a>" : <i>Double</i>,
        "<a href="#enablerealusermonitoring" title="EnableRealUserMonitoring">EnableRealUserMonitoring</a>" : <i>Boolean</i>,
        "<a href="#enduserapdexthreshold" title="EndUserApdexThreshold">EndUserApdexThreshold</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NewRelic::ApplicationSettings
Properties:
    <a href="#appapdexthreshold" title="AppApdexThreshold">AppApdexThreshold</a>: <i>Double</i>
    <a href="#enablerealusermonitoring" title="EnableRealUserMonitoring">EnableRealUserMonitoring</a>: <i>Boolean</i>
    <a href="#enduserapdexthreshold" title="EndUserApdexThreshold">EndUserApdexThreshold</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### AppApdexThreshold

The appex threshold for the New Relic application.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableRealUserMonitoring

Enable or disable real user monitoring for the New Relic application.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndUserApdexThreshold

The user's apdex threshold for the New Relic application.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the application in New Relic APM.

_Required_: Yes

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

