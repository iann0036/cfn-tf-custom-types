# Terraform::Google::ComputeProjectDefaultNetworkTier

Configures the Google Compute Engine
[Default Network Tier](https://cloud.google.com/network-tiers/docs/using-network-service-tiers#setting_the_tier_for_all_resources_in_a_project)
for a project.

For more information, see,
[the Project API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/projects/setDefaultNetworkTier).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ComputeProjectDefaultNetworkTier",
    "Properties" : {
        "<a href="#networktier" title="NetworkTier">NetworkTier</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::ComputeProjectDefaultNetworkTier
Properties:
    <a href="#networktier" title="NetworkTier">NetworkTier</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
</pre>

## Properties

#### NetworkTier

The default network tier to be configured for the project.
This field can take the following values: `PREMIUM` or `STANDARD`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

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

