# TF::AWS::PrometheusWorkspace

Manages an Amazon Managed Service for Prometheus (AMP) Workspace.

~> **NOTE:** This AWS functionality is in Preview and may change before General Availability release. Backwards compatibility is not guaranteed between Terraform AWS Provider releases.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::PrometheusWorkspace",
    "Properties" : {
        "<a href="#alias" title="Alias">Alias</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::PrometheusWorkspace
Properties:
    <a href="#alias" title="Alias">Alias</a>: <i>String</i>
</pre>

## Properties

#### Alias

The alias of the prometheus workspace. See more [in AWS Docs](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-onboard-create-workspace.html).

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

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

#### PrometheusEndpoint

Returns the <code>PrometheusEndpoint</code> value.

