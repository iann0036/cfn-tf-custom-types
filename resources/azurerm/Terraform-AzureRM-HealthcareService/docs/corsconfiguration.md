# Terraform::AzureRM::HealthcareService CorsConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowcredentials" title="AllowCredentials">AllowCredentials</a>" : <i>Boolean</i>,
    "<a href="#allowedheaders" title="AllowedHeaders">AllowedHeaders</a>" : <i>[ String, ... ]</i>,
    "<a href="#allowedmethods" title="AllowedMethods">AllowedMethods</a>" : <i>[ String, ... ]</i>,
    "<a href="#allowedorigins" title="AllowedOrigins">AllowedOrigins</a>" : <i>[ String, ... ]</i>,
    "<a href="#maxageinseconds" title="MaxAgeInSeconds">MaxAgeInSeconds</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#allowcredentials" title="AllowCredentials">AllowCredentials</a>: <i>Boolean</i>
<a href="#allowedheaders" title="AllowedHeaders">AllowedHeaders</a>: <i>
      - String</i>
<a href="#allowedmethods" title="AllowedMethods">AllowedMethods</a>: <i>
      - String</i>
<a href="#allowedorigins" title="AllowedOrigins">AllowedOrigins</a>: <i>
      - String</i>
<a href="#maxageinseconds" title="MaxAgeInSeconds">MaxAgeInSeconds</a>: <i>Double</i>
</pre>

## Properties

#### AllowCredentials

If credentials are allowed via CORS.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedHeaders

A set of headers to be allowed via CORS.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedMethods

The methods to be allowed via CORS.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedOrigins

A set of origins to be allowed via CORS.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxAgeInSeconds

The max age to be allowed via CORS.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

