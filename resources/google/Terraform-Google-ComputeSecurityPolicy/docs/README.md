# Terraform::Google::ComputeSecurityPolicy

A Security Policy defines an IP blacklist or whitelist that protects load balanced Google Cloud services by denying or permitting traffic from specified IP ranges. For more information
see the [official documentation](https://cloud.google.com/armor/docs/configure-security-policies)
and the [API](https://cloud.google.com/compute/docs/reference/rest/beta/securityPolicies).

Security Policy is used by [`google_compute_backend_service`](https://www.terraform.io/docs/providers/google/r/compute_backend_service.html#security_policy).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ComputeSecurityPolicy",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="rule.md">Rule</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#match" title="Match">Match</a>" : <i>[ <a href="match.md">Match</a>, ... ]</i>,
        "<a href="#config" title="Config">Config</a>" : <i>[ <a href="config.md">Config</a>, ... ]</i>,
        "<a href="#expr" title="Expr">Expr</a>" : <i>[ <a href="expr.md">Expr</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::ComputeSecurityPolicy
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="rule.md">Rule</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#match" title="Match">Match</a>: <i>
      - <a href="match.md">Match</a></i>
    <a href="#config" title="Config">Config</a>: <i>
      - <a href="config.md">Config</a></i>
    <a href="#expr" title="Expr">Expr</a>: <i>
      - <a href="expr.md">Expr</a></i>
</pre>

## Properties

#### Description

An optional description of this security policy. Max size is 2048.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the security policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The project in which the resource belongs. If it
is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of <a href="rule.md">Rule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Match

_Required_: No

_Type_: List of <a href="match.md">Match</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Config

_Required_: No

_Type_: List of <a href="config.md">Config</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expr

_Required_: No

_Type_: List of <a href="expr.md">Expr</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Fingerprint

Returns the <code>Fingerprint</code> value.

#### SelfLink

Returns the <code>SelfLink</code> value.

